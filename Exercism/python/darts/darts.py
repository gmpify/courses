
def score(x, y):
    distance = pow(((x * x) + (y * y)), 1/2)
    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0
