def is_triangle(sides):
    if 0 in sides or len(sides) != 3:
        return False
    
    for i in range(3):
        if sides[i] > (sides[(i + 1) % 3] + sides[(i + 2) % 3]):
            return False

    return True

def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3
