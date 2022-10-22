import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forwards():
    tim.forward(10)


def move_back():
    tim.backward(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(5)


def clear():
    screen.resetscreen()


screen.listen()
screen.onkeypress(move_forwards, 'w')
screen.onkeypress(move_back, "s")
screen.onkeypress(turn_right, "a")
screen.onkeypress(turn_left, "d")
screen.onkeypress(clear, "c")


screen.exitonclick()
