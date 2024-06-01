import pandas as pd
import numpy as np
import re
from textdistance import Jaccard
from collections import Counter

words = []
with open('books/alice_in_wonderland.txt', 'r') as f:
    file_name_data = f.read().lower()
    words = re.findall('\w+', file_name_data)

VOCAB = set(words)
word_freq_dict = Counter(words)

probs = {}
Total = sum(word_freq_dict.values())
for k in word_freq_dict.keys():
    probs[k] = word_freq_dict[k]/Total

def autocorrect(input_word):
    input_word = input_word.lower()
    if input_word in VOCAB:
        return input_word
    
    similarities = [1-(Jaccard(qval=2).distance(v, input_word)) for v in word_freq_dict.keys()]
    df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
    df = df.rename(columns={'index':'word', 0:'probability'})
    df['similarity'] = similarities
    output = df.sort_values(['similarity', 'probability'], ascending=False).head()

    return output

input_word = input()
print(autocorrect(input_word))