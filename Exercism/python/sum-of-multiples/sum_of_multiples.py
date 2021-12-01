def sum_of_multiples(limit, nums):
    multiples = []

    for num in nums:
        if num <= 0:
            continue

        multiples.extend(range(num, limit, num))

    return sum(set(multiples))
