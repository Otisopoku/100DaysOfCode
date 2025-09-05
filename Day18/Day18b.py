# implementing a random walk using the turtle module

from turtle import Turtle, Screen
import random


turtle = Turtle()
turtle.shape("classic")
turtle.width(4)

colors = [
    "red", "green", "blue", "yellow", "orange",
    "purple", "pink", "brown", "black",
    "cyan", "magenta", "lime", "indigo", "violet",
    "gold", "silver", "navy", "teal", "maroon"
]

directions = [0, 90, 180, 270]
for i in range(200):
    turtle.color(random.choice(colors))
    turtle.forward(20)
    turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()