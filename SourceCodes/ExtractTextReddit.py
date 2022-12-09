import os
import json
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

json_list = []
text = []
with open('RC_2009-05.txt', 'r', encoding='utf-8') as f:
    for line in f:
        a_dict = json.loads(line)
        json_list.append(a_dict)
        # print(a_dict)

for i in json_list:
    with open('RedditText.txt', 'a', encoding = 'utf-8') as f:
        for j in (i["body"]):
            if(isinstance(j, str)):
                print(j)
                f.write(str(j))
                        