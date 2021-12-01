import re

def abbreviate(words):
    words = words.replace('\'', '').replace('_', '')

    letters = re.findall(r"\b\w", words)
    return ''.join(letters).upper()
