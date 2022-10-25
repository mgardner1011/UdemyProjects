from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.font = FONT
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto((-280, 250))
        self.show_level()

    def show_level(self):
        self.write(f"Level: {self.level}", font=self.font)

    def level_up(self):
        self.clear()
        self.level += 1
        self.show_level()

    def game_over(self):
        self.goto((0, 0))
        self.write('GAME OVER!', align='center', font=self.font)
