import turtle
import pandas as pd

state = turtle.Turtle()

image = "./blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.register_shape(image)
screen.setup(height=491, width=725)
count = 0


# helper function to get the x and y coordinates 
def get_coor(x, y):
    print(x, y)
    

turtle.shape(image)
states_data = pd.read_csv("states.csv")

while count <= 50:

    answer_state = screen.textinput(title=f"Got {count} / 50 States correct", prompt="What's another state's name? ").capitalize()
    result: pd.DataFrame = states_data[states_data.states == answer_state]

    if not result.empty:
        x_cor = int(result.x.item())
        y_cor = int(result.y.item())
        
        state.penup()
        state.hideturtle()
        state.goto(x_cor, y_cor)
        state.write(f"{answer_state}")
        count += 1

screen.mainloop()