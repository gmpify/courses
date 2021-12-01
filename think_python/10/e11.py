def read_words(f):
    """
    Read word from file named f and generate a list with each word.
    It is expected that file contains one word per line.
    
    f: String

    return: List of strings
    """
    fin = open(f)
    
    t = []
    for word in fin:
        t.append(word.strip())
    
    fin.close()
    return t

def in_bisect(t, w):
    """
    Search wether given word w in list t. It uses bisection search
    algorithm.
    
    t: List of strings
    w: String

    return: Boolean
    """
    half = int(len(t) / 2)

    if w == t[half]:
        return True
    elif len(t) <= 1:
        return False
    
    if w < t[half]:
        return in_bisect(t[:half], w)
    else:
        return in_bisect(t[half:], w)

def find_reverse_pairs(t):
    """
    Look all words for its research pair. Returns a list of pair words.

    t: List of strings

    return: List of strings
    """
    pairs = []
    for word in t:
        r = word[::-1]
        if in_bisect(t, r):
            pairs.append((word, r))
    return pairs

def main():
    t = read_words("words.txt")
    w = find_reverse_pairs(t)
    print(w)

if __name__ == "__main__":
    main()
