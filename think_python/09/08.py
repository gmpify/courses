def is_palindrome(word):
    return word == word[::-1]

def find_correct_mileage(miles):
    m0 = str(miles)[-4:]
    m1 = str(miles + 1)[-5:]
    m2 = str(miles + 2)[1:-2]
    m3 = str(miles + 3)

    return (is_palindrome(m0) and is_palindrome(m1) and is_palindrome(m2) and is_palindrome(m3))

miles = 100_000
while miles <= 999_996:
    if find_correct_mileage(miles):
        print(miles)
    miles += 1
