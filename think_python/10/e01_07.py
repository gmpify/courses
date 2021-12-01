def nested_sum(t):
    """
    Sums nested lists of numbers, no matter how deeply they are nested

    t: Nested list of numbers

    return: Number
    """
    s = 0
    for nested in t:
        if isinstance(nested, list):
            s += nested_sum(nested)
        else:
            s += nested
    return s

def cumsum(t):
    """
    Perform a cumulative sum of a list, where each element
    correspond to the sum of all previous elements

    t: List of numbers

    return: New list of numbers
    """
    s = 0
    res = []
    for elem in t:
        s += elem
        res.append(s)
    return res

def middle(t):
    """
    For a given list, returns a new one with its middle elements,
    that is exclusing the first and last ones

    t: List

    return: New list
    """
    return t[1:-1]

def chop(t):
    """
    For a given list, remove the first and last element, by modifying it

    t: List

    return: None
    """
    t.pop(-1)
    t.pop(0)

def is_sorted(t):
    """
    Check wether a list of numbers is in sorted order
    
    t: List

    return: Boolean
    """
    return t == sorted(t)

def is_anagram(x, y):
    """
    Check wether two words are anagram

    x, y: String

    return: Boolean
    """
    return sorted(x) == sorted(y)

def has_duplicates(t):
    """
    Check if list contains duplicate elements

    t: List

    return: Boolean
    """
    prev = ""
    for elem in sorted(t):
        if prev == elem:
            return True
        prev = elem
    return False

def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))

    print(chop(t))
    print(t)

    print(is_sorted([1, 2, 3]))
    print(is_sorted(['b', 'a']))

    print(is_anagram("casa", "saca"))
    print(is_anagram("arara", "casaca"))

    print(has_duplicates([1, 2, 3, 4]))
    print(has_duplicates([1, 2, 2, 3]))

if __name__ == '__main__':
    main()

