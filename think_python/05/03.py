def is_triangle(a, b, c):
    """
    Check wether these sides can generate a triangle
    a, b, c: Integers with sides of triangle
    """
    if a > b + c or b > a + c or c > a + b:
        print('No')
    else:
        print('Yes')

def process_input():
    """
    Get input from user of a, b and c
    """
    a = int(input('Insert a: '))
    b = int(input('Insert b: '))
    c = int(input('Insert c: '))

    is_triangle(a, b, c)

process_input()
