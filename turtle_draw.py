from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')
tim.color('black')

sides = 3
colors = ['CornFlowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']

while sides < 11:
    for _ in range(sides):
        tim.forward(100)
        tim.right(360 / sides)
    sides +=1
    tim.color(random.choice(colors))


screen = Screen()
screen.exitonclick()
