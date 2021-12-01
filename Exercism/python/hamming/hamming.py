def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Can't calculate distance for strings with different length")

    distance = filter(lambda x: x[0] != x[1], zip(strand_a, strand_b))
    return len(list(distance))
