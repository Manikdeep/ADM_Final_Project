# Lemmatize the cleaned data

import sys
from nltk.stem import WordNetLemmatizer

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

lemmatizer = WordNetLemmatizer()

with open("cleanedTelegram.txt", 'r', encoding = 'utf-8') as m, open('lemmatizedData-Telegram.txt', 'w', encoding = 'utf-8') as n:
    for line in m:
        line = lemmatizer.lemmatize(line)
        print(line)
        n.write(str(line))
            