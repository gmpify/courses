def uses_only(word, allowed_letters):
    for letter in word:
        if letter not in allowed_letters:
            return False
    return True

allowed_letters = "acefhlo"

fin = open("words.txt")
for line in fin:
    word = line.strip()
    if uses_only(word, allowed_letters):
        print(word)
