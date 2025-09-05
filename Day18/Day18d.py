# Making a spirograph

import turtle
import random

t = turtle.Turtle()
t.speed("fastest")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def draw_spirograph(size_of_gap: int):
    for i in range(360 // size_of_gap):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)

draw_spirograph(3)

screen = turtle.Screen()
screen.exitonclick()