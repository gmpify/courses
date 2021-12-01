import math

def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a/x) / 2
        if y == x:
            return x
        x = y

def test_square_root():
    print(f"a   mysqrt(a)     math.sqrt(a)  diff")
    print(f"-   ---------     ------------  ----")
    a = 1
    while a < 9:
        my = mysqrt(a)
        other = math.sqrt(a)
        diff = abs(my - other)
        print(f"{a:.1f} {my:.11f} {other:.11f} {diff}")
        a += 1

test_square_root()
