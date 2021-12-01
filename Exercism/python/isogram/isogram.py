def is_isogram(string):
    chars = set()
    for c in string:
        if c in [' ', '-']:
            continue

        cl = c.lower()
        if cl not in chars:
            chars.add(cl)
        else:
            return False

    return True
