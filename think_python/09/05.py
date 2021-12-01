def uses_all(word, required_letters):
    for letter in required_letters:
        if letter not in word:
            return False
    return True

aeiou = "aeiou"
aeiouy = "aeiouy"

fin = open("words.txt")
aeiou_count = 0
aeiouy_count = 0
for line in fin:
    word = line.strip()
    if uses_all(word, aeiou):
        aeiou_count += 1
    if uses_all(word, aeiouy):
        aeiouy_count += 1
print(aeiou, aeiou_count)
print(aeiouy, aeiouy_count)
