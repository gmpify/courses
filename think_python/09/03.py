file_name = "words.txt"

def avoids(word, forbidden_letters):
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True

forbidden_letters = input("Insert forbidden letters: ").strip()

fin = open("words.txt")
allowed_words = 0
for line in fin:
    word = line.strip()
    if avoids(word, forbidden_letters):
        allowed_words += 1

print(f"Words without forbidden letters: {allowed_words}")
