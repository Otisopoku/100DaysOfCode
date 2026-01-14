from tkinter import *
import pandas as pd
import random as r


data_frame = pd.read_csv(filepath_or_buffer="data/french_words.csv", skiprows=0)
data_dict = data_frame.to_dict(orient="records")


    
def handle_right_button_click():
    word_pair = r.choice(data_dict)
    french_word = word_pair["French"]
    canvas.itemconfig(canvas_word, text=french_word)
    canvas.itemconfig(canvas_title, text="French")
    
    

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas object enables us to lay objects ontop of each other
canvas = Canvas(width=800, height=526)
front_card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 265, image=front_card_img)
canvas_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="donne", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=handle_right_button_click)
right_button.grid(row=1, column=1)



window.mainloop()