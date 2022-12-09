import os
import pandas as pd
import json
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

path = 'C:/Users/kaurm/Desktop/GSU/Advanced Data Mining/Project/RawData/Jan_files'

filelist = os.listdir(path)

path2 = []
for x in filelist:
    if x.endswith(".json"):
        path2.append(path + '/' + x )
        print(path2)

    result = list()
    for file in path2:
        f = open(file, encoding = 'utf-8')
        data = json.load(f)
        for i in data['messages']:
            if "text" not in i:
                continue
            with open('JanText.txt', 'a', encoding = 'utf-8') as f:
                for j in (i["text"]):
                    if(isinstance(j, str)):
                        print(j)   
                        f.write(str(j))