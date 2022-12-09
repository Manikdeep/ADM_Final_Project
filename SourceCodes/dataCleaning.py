# Cleans text - removes extra spaces, punctuations and emojis

import string
import re
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

with open("TelegramText.txt", 'r', encoding = 'utf-8') as r, open('cleanedTelegram.txt', 'w', encoding = 'utf-8') as o:
    for line in r:
        if line.strip():
            new_text = line.translate(str.maketrans(' ', ' ', string.punctuation))
            new_text = remove_emoji(new_text)
            print(new_text)
            o.write(str(new_text))
            
