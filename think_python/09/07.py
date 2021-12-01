import string

def find_triple_double(word):
    i = 0
    count = 0
    while i < (len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            count = 0
            i += 1

fin = open("words.txt")
for line in fin:
    word = line.strip()
    if find_triple_double(word):
        print(word)
