def find(word, letter, index):
    i = index
    while i < len(word):
        if word[i] == letter:
            return i
        i = i + 1
    return -1

def count(word, letter):
    count = 0
    index = 0
    while True:
        index = find(word, letter, index)
        if index == -1:
            break
        index += 1
        count += 1
    return count

print(count("banaaaaaaana", "a"))
