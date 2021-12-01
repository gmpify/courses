import re

def is_valid(isbn):
    pattern = re.compile('\d-?\d{3}-?\d{5}-?[\dX]')
    if not pattern.fullmatch(isbn):
        return False

    escaped_isbn = isbn.replace('-', '')

    isbn_sum = 0
    multiplier = 1
    for c in escaped_isbn[::-1]:
        term = 10 if c == 'X' else int(c)
        isbn_sum += term * multiplier
        multiplier += 1

    return isbn_sum % 11 == 0
