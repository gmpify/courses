def check_fermat(a, b, c, n):
    if n > 2 and (pow(a, n) + pow(b, n) == pow(c, n)):
        print("Holly smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")

def process_input():
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    c = int(input("Enter value for c: "))
    n = int(input("Enter value for n: "))

    check_fermat(a, b, c, n)

process_input()
