def saddle_points(matrix):
    if len(set(map(len, matrix))) > 1:
        raise ValueError('Assymetric matrix')

    candidates = []
    for r, row in enumerate(matrix):
        for c, column in enumerate(zip(*matrix)):
            if matrix[r][c] == max(row) and matrix[r][c] == min(column):
                candidates.extend([{"row": r + 1, "column": c + 1}])

    return candidates
