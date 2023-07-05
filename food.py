from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.create_new_food()

    def create_new_food(self):
        x_position = randint(-280, 280)
        y_position = randint(-280, 280)
        self.goto(x_position, y_position)
