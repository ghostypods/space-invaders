from turtle import Turtle


class Invader(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(270)
        self.goto(x, y)
        self.x_move = 3
        self.active = True

    def move(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())

    def bounce_x(self):
        self.x_move *= -1
