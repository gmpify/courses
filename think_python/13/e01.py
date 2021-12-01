import sys
import string

def read_book(name):
    f = open(name)

    words = dict()
    # TODO: use enumerate to make this a little bit better https://stackoverflow.com/questions/2081836/reading-specific-lines-only
    process_line = False
    for line in f:
        if '*** START OF THIS PROJECT GUTENBERG EBOOK' in line:
            process_line = True
            continue
        if '*** END OF THIS PROJECT GUTENBERG EBOOK' in line:
            break
        if not process_line:
            continue

        sanitized_line = string.translate(line, None, string.punctuation)
        for word in string.split(sanitized_line):
            w = word.lower()
            words[w] = words.setdefault(w, 0) + 1

    return words

def print_common_words(words, number=20):
    common_words = sorted(words.items(), key=lambda x: x[1], reverse=True)[0:(number - 1)]
    print("Common words:")
    for w in common_words:
        print(w[0], w[1])

def print_total_words(words):
    print("Total words:")
    print(len(words))

def main():
    words = read_book(sys.argv[1])
    print_total_words(words)
    print_common_words(words)

if __name__ == '__main__':
    main()
