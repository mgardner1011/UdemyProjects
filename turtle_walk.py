import turtle as t
import random

t.colormode(255)
angles = [0, 90, 180, 270]
tim = t.Turtle()
tim.pensize(15)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def walk(angle):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(angle))


for _ in range(200):
    walk(angles)


screen = t.Screen()
screen.exitonclick()
