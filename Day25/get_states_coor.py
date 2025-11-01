import turtle
import pandas as pd

background = "./blank_states_img.gif"

states_dict = {
    "states": [],
    "x": [],
    "y": []
}

screen = turtle.Screen()
screen.register_shape(background)
turtle.shape(background)
screen.setup(height=491, width=725)

def get_coor(x, y): 
    state_name = turtle.textinput(title="State Name", prompt="Name of State clicked")
    if state_name:
        states_dict["states"].append(state_name.capitalize())
        states_dict["x"].append(x)
        states_dict["y"].append(y)
        t = turtle.Turtle()
        t.shape("turtle")
        t.penup()
        t.goto(x,y)
        
        print(f"{state_name} added at ({x}, {y})")
        
screen.onscreenclick(get_coor)
screen.mainloop()


my_states = pd.DataFrame(states_dict)
my_states.to_csv("states.csv", index=False)
print("States and coordinates saved to states.csv")

