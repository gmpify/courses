def check_palindrome(a1, a2):
    as1 = str(a1).zfill(2)
    as2 = str(a2).zfill(2)

    return as1 == as2[::-1]

diff = 0
while diff <= 99:
    ages = []
    age = 0
    while age <= 99:
        mother_age = age + diff
        if mother_age > 99:
            break
        if check_palindrome(age, mother_age):
            ages.append(age)
        age += 1
    if len(ages) == 8:
        print(ages, diff)
    diff += 1
