def rotate_word(word, rotation):
    new_string = ""
    for c in word:
        from_a = ord(c) - ord("a")
        new_char = (from_a + rotation) % (ord("z") - ord("a"))
        new_string += chr(new_char + ord("a"))
    return new_string

def read_words(f):
    """
    Read words from file f and return a dictionary with all of them

    f: string

    returns: dict
    """
    fin = open(f)

    d = dict()
    for word in fin:
        d[word.strip().lower()] = True

    fin.close()
    return d

def find_rotate_pairs(t):
    """
    Find all rotate pairs from word list w and print them.
    
    w: dict

    Return: None
    """
    for word in t:
        for i in range(1, 23):
            rotated = rotate_word(word, i)
            if rotated in t:
                print(word, rotated)
            i += 1

def main():
    t = read_words('words.txt')
    find_rotate_pairs(t)

if __name__ == '__main__':
    main()
