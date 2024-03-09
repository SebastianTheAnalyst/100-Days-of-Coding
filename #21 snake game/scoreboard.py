from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write_score()

    def write_score(self):
        self.write(arg=f"Score: {self.score}", align='center', font=('Arial', 18, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align='center', font=('Arial', 24, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()
