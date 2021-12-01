points = {
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
    ("D", "G"): 2,
    ("B", "C", "M", "P"): 3,
    ("F", "H", "V", "W", "Y"): 4,
    ("K"): 5,
    ("J", "X"): 8,
    ("Q", "Z"): 10
}
points_lookup = {
    letter: value
    for letters, value in points.items()
    for letter in letters
}

def score(word):
    return sum(points_lookup[x] for x in word.upper())
