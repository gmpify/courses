import turtle

def koch(t, length):
    if length < 3:
        t.fd(length)
        return
    koch(t, int(length/3))
    t.lt(60)
    koch(t, int(length/3))
    t.rt(120)
    koch(t, int(length/3))
    t.lt(60)
    koch(t, int(length/3))

bob = turtle.Turtle()

koch(bob, 300)

turtle.mainloop()
