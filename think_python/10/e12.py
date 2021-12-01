from e10 import read_words, in_bisect

def interlock(t, w):
    """
    Check whether word w is result of two interlocked words
    
    t: List of strings
    w: String

    returns: List of Strings
    """
    return in_bisect(t, w[::2]) and in_bisect(t, w[1::2])

def main():
    t = read_words("words.txt")
    for word in t:
        if interlock(t, word):
            print(word, word[::2], word[1::2])

if __name__ == "__main__":
    main()
