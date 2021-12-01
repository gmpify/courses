def count_partitions(n, m):
    if m == 1:
        return 1
    if n < 0:
        return 0
    return count_partitions(n - m, m) + count_partitions(n, m - 1)
