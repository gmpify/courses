import re
from collections import defaultdict

def count_words(sentence):
    result = defaultdict(int)

    for word in re.findall(r"([a-zA-Z0-9]+(?:'[a-zA-Z0-9]+)?)", sentence):
        result[word.lower()] += 1

    return result
