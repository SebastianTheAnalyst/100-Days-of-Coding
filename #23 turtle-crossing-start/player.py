from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(2)
        self.color("white")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def walking_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def walking_down(self):
        self.setheading(90)
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # reaching the other side:
    def is_at_finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False







