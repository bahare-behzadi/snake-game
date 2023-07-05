from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]


    def create_snake(self):
        for number in range(0, 3):
            position = (0 - (number * 20), 0)
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        new_turtle.goto(position)
        new_turtle.color("blue")
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            self.segments[segment].penup()
            new_x_position = self.segments[segment - 1].xcor()
            new_y_position = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x_position, new_y_position)
        self.snake_head.forward(20)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() !=0:
            self.snake_head.setheading(180)
