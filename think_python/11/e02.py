def invert_dict(d):
    """
    Inverts a dictionary, returning a map from val to a list of keys.

    If the mapping key->val appears in d, then in the new dictionary
    val maps to a list that includes key.

    d: dict

    Returns: dict
    """
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse

if __name__ == '__main__':
    d = {'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
    print(d)
    print(invert_dict(d))
