import turtle
import math

bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n, arc=360):
    angle = arc/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circuference = 2 * math.pi * r
    n = 100
    length = circuference / n
    polygon(t, length, n)

def arc(t, r, angle):
    circuference = 2 * math.pi * r * angle / 360
    n = 100
    length = circuference / n
    polygon(t, length, n, angle)

arc(bob, 100, 180)

turtle.mainloop()
