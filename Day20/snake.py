from turtle import Turtle

SNAKE_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

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