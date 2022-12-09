from wordcloud import WordCloud
from collections import Counter
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

wc = WordCloud()

counts_all = Counter()

with open('lemmatizedData-Telegram.txt', 'r', encoding = 'utf-8') as f:
    for line in f:  
        counts_line = wc.process_text(line)
        counts_all.update(counts_line)
        print(counts_all)

wc.generate_from_frequencies(counts_all)
wc.to_file('WordCloudTelegram.png')