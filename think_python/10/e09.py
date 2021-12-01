import time

def try_append(f):
    w = []
    for l in f:
        word = l.strip()
        w.append(word)
    return w

def try_idiom(f):
    w = []
    for l in f:
        word = l.strip()
        w += [word]
    return w

def main():
    fin = open("words.txt")

    fin.seek(0, 0)
    start_time = time.time()
    t = try_append(fin)
    diff = time.time() - start_time
    print("Using append took", diff)
    print(t[:10])

    fin.seek(0,0)
    start_time = time.time()
    t = try_idiom(fin)
    diff = time.time() - start_time
    print("Using idiom took", diff)
    print(t[:10])

    fin.close()

if __name__ == "__main__":
    main()
