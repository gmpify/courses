def square(number):
    if number < 1 or number > 64:
        raise ValueError('Number must be between 1 and 64')

    if number == 1:
        return 1
    return 2 * square(number - 1)

def total():
    return square(64) * 2 - 1
