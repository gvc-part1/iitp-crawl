import time
import os
import sys
import re
import traceback

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from tqdm import tqdm
import pandas as pd

class Mining():
    def __init__(self, end_page=10):
        self.end_page = int(end_page) if int(end_page) > 0 else 10
        self.links = []
        self.df_list = []
        if os.path.exists("./mining_crawl.json"):
            self.df_prev = pd.read_json("./mining_crawl.json")
        else:
            self.df_prev = pd.DataFrame(columns=["title", "date", "body"])

    def get_links(self):
        try:
            driver = uc.Chrome()
            driver.execute_script("Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});")
            for page_num in range(self.end_page):
                driver.get(f"https://www.mining.com/commodity/copper/page/{page_num + 1}")
                try:
                    elements = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='latest-section']//h3/a")))
                except:
                    print("timeout")
                    pass
                for element_a in elements:
                    link = element_a.get_attribute("href")
                    print(link)
                    self.links.append(link)
            return self
        except Exception as e:
            print(e)
            print(traceback.print_exc())
            pass
        finally:
            driver.close()
            driver.quit()

    def download(self):
        driver = uc.Chrome()
        driver.execute_script("Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});")
        try:
            for link in tqdm(self.links):
                try:
                    driver.get(link)
                    post_title = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//h1")))
                    post_title = post_title.text
                    post_timestamp = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@id='single-post']//div[@class='post-meta mb-4']")))
                    post_timestamp = post_timestamp.text
                    post_timestamp = post_timestamp.split(" | ")[1]
                    post_body = []
                    body_container = WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located((By.XPATH, "//div[@class='container-fluid my-4']/div[@class='container'][2]"))
                    )
                    body_p = body_container.find_elements(By.XPATH, ".//p")
                    for p in body_p:
                        post_body.append(p.text)
                    parser = {
                      "title": post_title,
                      "date": post_timestamp,
                      "body": post_body
                    }
                    if self.df_prev.empty or (not str(post_title) in self.df_prev.title.values):
                        self.df_list.append(parser)
                        self.save_df()
                except Exception as e:
                    print(e)
                    print(traceback.print_exc())
        finally:
            driver.close()
            driver.quit()

    def save_df(self):
        df = pd.concat([self.df_prev, pd.DataFrame(self.df_list)], ignore_index=True)
        df.to_json("./mining_crawl.json", orient="records")

if __name__ == "__main__":
    mine = Mining(2)
    mine.get_links().download()
