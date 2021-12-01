def is_abecedarian(word):
    prev_char = word[0]
    for letter in word:
        if ord(prev_char) > ord(letter):
            return False
        prev_char = letter
    return True

fin = open("words.txt")
abecedarian_count = 0
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        abecedarian_count += 1

print(abecedarian_count)
