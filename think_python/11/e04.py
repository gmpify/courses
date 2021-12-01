def has_duplicates(t):
    """
    Check if list contains duplicate elements

    t: List

    return: Boolean
    """
    d = dict()
    for elem in t:
        if elem in d:
            return True
        d[elem] = ""
    return False

def main():
    print(has_duplicates([1, 2, 3, 4]))
    print(has_duplicates([1, 2, 2, 3]))

if __name__ == '__main__':
    main()
