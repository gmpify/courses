def steps(number):
    if number < 1:
        raise ValueError('number must be bigger or equal 1')

    if number == 1:
        return 0

    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1

    return 1 + steps(number)
