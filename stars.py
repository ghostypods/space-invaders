from turtle import Turtle


class Stars(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.1, stretch_len=0.1)
        self.color('white')
        self.penup()
        self.goto(x, y)
