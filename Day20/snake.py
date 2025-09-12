from turtle import Turtle
from enum import Enum

SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Direction(Enum):
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_segments: list[Turtle] = []

        for position in SNAKE_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.snake_segments.append(segment)

        self.head = self.snake_segments[0]

    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[i - 1].xcor()
            new_y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != Direction.DOWN.value:
            self.head.setheading(Direction.UP.value)

    def down(self):
        if self.head.heading() != Direction.UP.value:
            self.head.setheading(Direction.DOWN.value)

    def left(self):
        if self.head.heading() != Direction.RIGHT.value:
            self.head.setheading(Direction.LEFT.value)

    def right(self):
        if self.head.heading() != Direction.LEFT.value:
            self.head.setheading(Direction.RIGHT.value)