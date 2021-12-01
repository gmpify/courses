def classify(number):
    if number <= 0:
        raise ValueError('Number must be positive')

    factors = [x for x in range(1, number) if number % x == 0]
    factors_sum = sum(factors)
    if factors_sum == number:
        return 'perfect'
    elif factors_sum > number:
        return 'abundant'
    else:
        return 'deficient'
