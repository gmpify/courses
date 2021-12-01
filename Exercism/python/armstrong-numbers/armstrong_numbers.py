def is_armstrong_number(number):
    digits = str(number)
    number_of_digits = len(digits)

    sum_of_powers = 0
    for digit in digits:
        sum_of_powers = sum_of_powers + int(digit)**number_of_digits

    return sum_of_powers == number
