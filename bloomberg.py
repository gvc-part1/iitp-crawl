import time
import os
import sys
import re

import pandas as pd
import requests
from lxml import etree, html
from tqdm import tqdm
from playwright.sync_api import (
    sync_playwright,
    TimeoutError as PlaywrightTimeoutError,
)


class Bloomberg():
    def __init__(self):
        self.links = []
        self.df_list = []
        if os.path.exists("./bloomberg_crawl.json"):
            self.df_prev = pd.read_json("./bloomberg_crawl.json")
        else:
            self.df_prev = pd.DataFrame(columns=["title", "title_sub", "point1", "point2", "date", "category", "category_sub", "body"])

    def get_links(self, *dates):
        for raw_d in dates:
            y, m = raw_d.split("-")
            y = int(y)
            m = int(m)
            response = requests.get(f"https://www.bloomberg.com/feeds/bbiz/sitemap_{y}_{m}.xml")
            if response.status_code != 200:
                raise "Error"
            root = etree.fromstring(response.content)
            children = [
                "/".join(x[0].text.split("/")[5:])
                for x in root
                if re.match(
                    r"https:\/\/www\.bloomberg\.com\/news\/articles\/\d{4}-\d{2}-\d{2}\/.+",
                    x[0].text,
                )
            ]
            for child in children:
                self.links.append(child)
        return self
                

    def download(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            for link in tqdm(self.links):
                start = time.perf_counter()
                self.download_link(browser, link)
                t = int(10 - time.perf_counter() + start)
                if t <= 0:
                    t = 1
                time.sleep(t)
            print("블룸버그 크롤링이 완료되었습니다.")
            browser.close()

    def download_link(self, browser, link_id):
        try:
            context = browser.new_context()
            page = context.new_page()
            page.add_init_script(
                "Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});"
            )
            try:
                page.goto(f"https://www.bloomberg.com/news/articles/{link_id}", wait_until='networkidle', timeout=20000)
            except:
                pass
            # check 404
            page_title = page.title()
            if page_title == "404. Page Not Found - Bloomberg":
                print("페이지가 존재하지 않습니다.")
                return
            while page.title() == "Bloomberg - Are you a robot?":
                print("크롤링 방지 스크립트에 걸렸습니다. 해제 후 기다려 주세요...")
                time.sleep(30)
            paywall = page.locator(
                "//div[@data-testid='premium-label']"
            ).is_visible()
            if paywall:
                print("유료 기사입니다.")
                return
            content = page.content()
            self.extract(content)
        except KeyboardInterrupt:
            print('크롤링이 취소되었습니다.')
            try:
                sys.exit(1)
            except SystemExit as e:
                os._exit(e.code)
            finally:
                browser.close()
        except Exception as e:
            print(e)
            print("오류가 발생했습니다.")
        finally:
            page.close()
            context.close()

    def extract(self, content):
        parser = html.fromstring(content)
        # 제목
        title = parser.xpath("//main//article//h1")[0].text_content()
        # 요약
        try:
            title_sub = parser.xpath(
                '//div[starts-with(@class,"hed-and-dek__")]//div[starts-with(@class,"dek__")/p]'
            )[0].text_content()
        except:
            title_sub = None
        # 포인트
        point2 = None
        try:
            point1 = parser.xpath('//div[starts-with(@class,"abstract-item-text__")]')[
                0
            ].text_content()
            try:
                point2 = parser.xpath(
                    '//div[starts-with(@class,"abstract-item-text__")]'
                )[1].text_content()
            except:
                point2 = None
        except:
            point1 = None
        # 날짜
        date = parser.xpath('//time[@itemprop="datePublished"]/@datetime')[0]
        # 대분류
        category = parser.xpath('//span[starts-with(@class,"brand__")]')[
            0
        ].text_content()
        # 소분류
        try:
            category_sub = parser.xpath('//div[starts-with(@class,"pillar")]')[
                0
            ].text_content()
        except:
            category_sub = None
        # 본문 텍스트 수집
        body_text_nodes = parser.xpath('//main//article//div[@class="body-content fence-body"]//p')
        body = "\n".join(
            [x.text_content().encode("ascii", "ignore").decode().replace(u"\u2018", "'").replace(u"\u2019", "'") for x in body_text_nodes]
        )
        if (not str(title) in self.df_prev.title.values) or self.df_prev.empty:
            self.df_list.append({
                "title": str(title),
                "title_sub": str(title_sub),
                "point1": str(point1),
                "point2": str(point2),
                "date": date,
                "category": str(category),
                "category_sub": str(category_sub),
                "body": str(body)
            })
            self.save_df()

    def save_df(self):
        df = pd.concat([self.df_prev, pd.DataFrame(self.df_list)], ignore_index=True)
        df.to_json("./bloomberg_crawl.json", orient="records")

if __name__ == "__main__":
    bloom = Bloomberg()
    bloom.get_links("2022-09").download()
