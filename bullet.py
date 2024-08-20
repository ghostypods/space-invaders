from turtle import Turtle
from time import sleep


class Bullet(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.2, stretch_len=0.5)
        self.color(color)
        self.penup()
        self.goto(*position)
        self.y_move = 6

    def move(self):
        # new_y = self.ycor() + self.y_move
        # self.goto(self.xcor(), new_y)
        self.forward(self.y_move)
