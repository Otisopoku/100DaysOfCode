import turtle 
import random

my_turtle = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
    

directions = [0, 90, 180, 270]
my_turtle.pensize(15)
my_turtle.speed("fastest")

for i in range(200):
    my_turtle.color(random_color())
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(directions))


screen = turtle.Screen()
screen.exitonclick()