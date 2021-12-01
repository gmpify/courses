def read_words(f):
    """
    Read words from a file f and returns a dictionary containing an array of anagrams.

    f: string

    returns: dict
    """
    fin = open(f)
    d = dict()

    for line in fin:
        word = line.strip()
        key = tuple(sorted(word))
        d.setdefault(key, []).append(word)
    
    return(d)

def filter_words(w):
    """
    Receive a dictionary w containing all words, aggregated by the tuple of letters that it has. Print the anagrams

    w: dict

    returns:
    """
    d = dict()
    for i in filter(lambda x: len(x) == 8, w):
        d[i] = w[i]
    
    s = sorted(d.values(), key=lambda x: len(x), reverse=True)
    
    for i in filter(lambda x: len(x) >= 2, s):
        print(i)

def main():
    words = read_words("words.txt")
    filter_words(words)

if __name__ == '__main__':
    main()
