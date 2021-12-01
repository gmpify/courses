import pronounce

def find_homophone(word, d):
    word_no_first = word[1:]
    if word_no_first not in d or d[word] != d[word_no_first]:
        return

    word_no_second = word[0] + word[2:]
    if word_no_second not in d or d[word] != d[word_no_second]:
        return

    print(word, d[word])
    print(word_no_first, d[word_no_first])
    print(word_no_second, d[word_no_second])

if __name__ == '__main__':
    d = pronounce.read_dictionary('c06d')
    for word in d:
        if len(word) != 5:
            continue
        find_homophone(word, d)
