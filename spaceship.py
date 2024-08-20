from turtle import Turtle


class Spaceship(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("triangle")
        self.color('white')
        self.penup()
        self.setheading(90)
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())
