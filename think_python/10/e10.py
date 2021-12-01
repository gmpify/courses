def read_words(f):
    """
    Read word file and generate a list with each word. It is expected
    that file contains one word per line.
    
    f: File name

    return: List
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

def main():
    t = read_words("words.txt")
    print(in_bisect(t, "houseasdad"))

if __name__ == "__main__":
    main()
