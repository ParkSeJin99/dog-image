#!python
print("Content-Type: text/html")
print()
import pandas as pd
import requests
from tqdm import tqdm 
import json

data=pd.read_csv("/content/lotto2.csv",encoding='CP949')

data

num_list = list(data['당첨번호1']) + list(data['당첨번호2']) + list(data['당첨번호3']) + list(data['당첨번호4']) + list(data['당첨번호5']) + list(data['보너스'])

from collections import Counter 
count = Counter(num_list)
common_num_45 = count.most_common(45)

print(count)

print(common_num_45)

common_num_10=count.most_common(10)
print(common_num_10)

data.sort_values(by=['1등 당첨금액'], axis=0, ascending=False).head(10)
