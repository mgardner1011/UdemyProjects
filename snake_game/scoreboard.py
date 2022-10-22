from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.ht()
        self.goto(x=0, y=280)
        self.score = 0
        self.print_score()

    def print_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
