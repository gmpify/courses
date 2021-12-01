def slices(series, length):
    if length > len(series):
        raise ValueError("Provided length bigger than series length")
    if length <= 0:
        raise ValueError("Provided length should be positive")

    return [series[i:i+length] for i in range(len(series) - length + 1)]
