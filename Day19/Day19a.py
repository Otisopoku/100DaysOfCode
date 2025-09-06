from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards) # when passing a function as input,
# we don't add the parenthesis at the end
screen.exitonclick()