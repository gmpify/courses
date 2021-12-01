import polygon
import turtle
import math

def pie(t, n, r):
    """
    Draw a pie with the given radius and sides.

    t: Turtle
    n: sides
    r: radius
    """
    angle = 360/n
    outer_angle = (180 - angle)/2
    outer_side = r / math.sin(math.radians(outer_angle)) * math.sin(math.radians(angle))
    for _ in range(n):
        t.fd(r)
        t.lt(180 - outer_angle)
        t.fd(outer_side)
        t.lt(180 - outer_angle)
        t.fd(r)
        t.rt(180)

if __name__ == '__main__':
    bob = turtle.Turtle()

    bob.pu()
    bob.bk(250)
    bob.pd()

    bob.lt(360/5)
    pie(bob, 5, 100)
    bob.rt(360/5)

    bob.pu()
    bob.fd(250)
    bob.pd()

    bob.lt(360/6)
    pie(bob, 6, 100)
    bob.rt(360/6)

    bob.pu()
    bob.fd(250)
    bob.pd()

    bob.lt(360/7)
    pie(bob, 7, 100)
    bob.rt(360/7)

    turtle.mainloop()

