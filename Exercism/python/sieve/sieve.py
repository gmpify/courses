def primes(limit):
    numbers = list(range(2, limit + 1))

    i = 0
    while i < len(numbers):
        prime = numbers[i]
        j = prime * 2
        while j <= limit:
            if j in numbers:
                numbers.remove(j)
            j += prime
        i += 1

    return numbers
