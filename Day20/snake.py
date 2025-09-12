from turtle import Turtle

SNAKE_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEADING_POSITIONS = {"north": 90, "south": 270, "east": 0, "west": 180}

class Snake:

    def __init__(self):
        self.snake_segments: list[Turtle] = []

        for position in SNAKE_POSITIONS:
            segment1 = Turtle("square")
            segment1.color("white")
            segment1.penup()
            segment1.goto(position)
            self.snake_segments.append(segment1)

    def move(self):
        for i in range(len(self.snake_segments) -1, 0, -1):
            new_x = self.snake_segments[i - 1].xcor()
            new_y = self.snake_segments[i - 1].ycor()
            
            self.snake_segments[i].penup()
            self.snake_segments[i].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_segments[0].heading() != 270:
            self.snake_segments[0].setheading(90)

    def down(self):
        if self.snake_segments[0].heading() != 90:
            self.snake_segments[0].setheading(270)

    def left(self):
        if self.snake_segments[0].heading() != 0:
            self.snake_segments[0].setheading(180)

    def right(self):
        if self.snake_segments[0].heading() != 180:
            self.snake_segments[0].setheading(0)