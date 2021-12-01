import polygon
import turtle

def petal(bob, radius, angle):
    for _ in range(2):
        polygon.arc(bob, radius, angle)
        bob.lt(180 - angle)

def flower(bob, radius, number_of_petals, angle):
    for _ in range(number_of_petals):
        petal(bob, radius, angle)
        bob.lt(360/number_of_petals)

if __name__ == '__main__':
    bob = turtle.Turtle()

    flower(bob, 150, 7, 50)
    
    turtle.mainloop()

