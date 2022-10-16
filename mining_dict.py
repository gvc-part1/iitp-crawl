# 패키지 import

import pandas as pd
import re
import itertools
import os
import json

import math
import numpy as np

from lxml import html

from pathlib import Path

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

from tqdm import tqdm



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

