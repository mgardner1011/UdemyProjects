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
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.print_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.print_score()
