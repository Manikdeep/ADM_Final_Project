#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
import json
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

path = 'C:/Users/kaurm/Desktop/GSU/Advanced Data Mining/Project/RawDataTelegram'

filelist = os.listdir(path)
filelist

path2 = []
for x in filelist:
    if x.endswith('_files'):
        path2.append(path + '/' + x + '/')
print(path2)

files = []
for i in path2:        
    for file in os.listdir(i):
        if file.endswith(".json"):
            files.append(os.path.join(i, file))

    result = list()
    for file in files:
        f = open(file, encoding = 'utf-8')
        data = json.load(f)
        for i in data['messages']:
            if "text" not in i:
                continue
            with open('TelegramText.txt', 'a', encoding = 'utf-8') as f:
                for j in (i["text"]):
                    if(isinstance(j, str)):
                        print(j)   
                        f.write(str(j))
