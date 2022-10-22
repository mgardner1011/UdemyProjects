import turtle as t
import random

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
              (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
              (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.hideturtle()
x_pos = -300
y_pos = -300
tim.setposition(x_pos, y_pos)

for _ in range(100):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if tim.xcor() >= 200:
        y_pos += 50
        tim.setposition(x_pos, y_pos)


screen = t.Screen()
screen.exitonclick()
