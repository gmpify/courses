def is_power(a, b):
    if b == 1 and a != 1:
        return False
    if a == 1:
        return True
    return (a % b == 0) and is_power(a/b, b)

print(is_power(1, 2))
print(is_power(4, 2))
print(is_power(4, 3))
print(is_power(125, 5))
