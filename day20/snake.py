from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-21, 0), (-42, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            michael = Turtle(shape="square")
            michael.color('white')
            michael.penup()
            michael.goto(position)
            self.body_parts.append(michael)

    def move(self):
        for seg_num in range(len(self.body_parts) - 1, 0, -1):
            new_x = self.body_parts[seg_num - 1].xcor()
            new_y = self.body_parts[seg_num - 1].ycor()
            self.body_parts[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
