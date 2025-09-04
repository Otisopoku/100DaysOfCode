# Drawing different sized shapes using turtle

from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("classic")
my_turtle.color("green")
my_turtle.width(3)

TOTAL_ANGLE= 360


colors = ["green", "red", "yellow", "black", "purple", "orange", "brown", "blue"]
expand = 0

for side in range(3, 11):
    angle = TOTAL_ANGLE / side
    if angle.is_integer():
        my_turtle.color(random.choice(colors))
        for i in range(side):
            my_turtle.forward(100)
            my_turtle.right(angle)
        





screen = Screen()
screen.exitonclick()