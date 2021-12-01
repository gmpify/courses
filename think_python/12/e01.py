def most_frequent(s):
        """
        Print the letters in string s descresing order of frequency

        s: string

        Returns: None
        """
        count = dict()
        for l in s:
                count[l] = count.setdefault(l, 0) + 1
    
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        for l in sorted_count:
                print(l[0])

def main():
        most_frequent("testesteaisjdaiosjdaiudhaiusdhaiushd")

if __name__ == "__main__":
        main()
