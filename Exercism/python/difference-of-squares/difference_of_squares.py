def square_of_sum(number):
    number_sum = sum(range(1, number + 1))
    return pow(number_sum, 2)

def sum_of_squares(number):
    if number == 1:
        return 1
    return pow(number, 2) + sum_of_squares(number - 1)

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
