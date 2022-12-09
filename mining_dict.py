# 패키지 import

import pandas as pd
import json



# json 파일 df화

with open('mining_crawl.json', 'r') as json_m:
    dic_mining = json.load(json_m)

df = pd.DataFrame(dic_mining)
df = df_mining.drop(df_mining.columns[0], axis=1)


# corpus dictionary 생성

corpus = {}

for i in range(0, len(df)):
    m = str(df['date'][i])[5:7]
    t = df['title'][i]
    b = df['body'][i]
    temp = b
    temp.insert(0, t)
    article = {'month': m, 'text': temp}
    corpus['article_' + str(i)] = article

