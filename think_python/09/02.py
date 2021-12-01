file_name = "words.txt"

def has_no_e(word):
    return not "e" in word

fin = open("words.txt")
words_with_e = 0
words_without_e = 0
for line in fin:
    word = line.strip()
    words_with_e += 1
    if has_no_e(word):
        print(word)
        words_without_e += 1

ratio = words_without_e/words_with_e
print(f"{(ratio * 100):.2f}%")
