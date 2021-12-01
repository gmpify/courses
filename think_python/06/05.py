def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(5, 2))
print(gcd(1000, 50))
print(gcd(1200, 999))
