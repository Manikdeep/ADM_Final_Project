import re
import sys
from nltk.corpus import stopwords

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
 
frequency = {}
document_text = open('lemmatizedData-Telegram.txt', 'r', encoding='utf-8')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

en_stops = set(stopwords.words('english'))
  
for word in match_pattern:
    if word not in en_stops:
        count = frequency.get(word,0)
        frequency[word] = count + 1
 
most_frequent = dict(sorted(frequency.items(), key=lambda elem: elem[1], reverse=True))
most_frequent_count = most_frequent.keys()

with open('wordFrequencyTelegram.txt', 'a', encoding = 'utf-8') as f:
    for words in most_frequent_count:
        print(words, most_frequent[words])
        f.write(words+' '+str(most_frequent[words])+'\n')
