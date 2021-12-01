def find_palindromes(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError('min_factor must be less than max_factor')

    palindromes = {}
    for x in range(min_factor, max_factor + 1):
        for y in range(x, max_factor + 1):
            product = x * y
            if str(product) == str(product)[::-1]:
                if not product in palindromes:
                    palindromes[product] = []
                palindromes[product].append([x, y])

    return palindromes


def largest(min_factor, max_factor):
    palindromes = find_palindromes(min_factor, max_factor)

    if not palindromes:
        return (None, [])

    largest = sorted(palindromes)[-1]
    return (largest, palindromes[largest])


def smallest(min_factor, max_factor):
    palindromes = find_palindromes(min_factor, max_factor)

    if not palindromes:
        return (None, [])

    smallest = sorted(palindromes)[0]
    return (smallest, palindromes[smallest])
