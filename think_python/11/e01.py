def read_words(f):
    """
    Read words from file f and return a dictionary with all of them

    f: File name

    returns: Dictionary
    """
    fin = open(f)

    d = dict()
    for word in fin:
        d[word.strip()] = 0

    fin.close()
    return d

def main():
    t = read_words('words.txt')
    word = "houseasd"
    print(word in t)

if __name__ == '__main__':
    main()
