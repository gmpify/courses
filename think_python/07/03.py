import math

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def estimate_pi():
    total = 0

    k = 0
    constant = 2 * math.sqrt(2) / 9801
    while True:
        summation = (factorial(4 * k) * (1103 + 26390 * k)) / (pow(factorial(k), 4) * pow(396, 4 * k))
        term = constant * summation
        total += term

        if abs(term < 1e-15):
            break
        k += 1
    return 1 / total

print(estimate_pi())
