from tkinter import *
import pandas as pd
import random as r

#NB: With tkiinter, we use the windows.after method to set timer. Using the time module ie: time.sleep will freeze the UI

BACKGROUND_COLOR = "#B1DDC6"

data_frame = pd.read_csv(filepath_or_buffer="data/french_words.csv", skiprows=0)
data_dict = data_frame.to_dict(orient="records")

word_pair = r.choice(data_dict)
flip_timer = None # to handle and cancel timer in situations where the user clicks on the correct or wrong button before the timer ends so a new
# 5 seconds timer will be initiated on the next card flip



def show_new_card():
    global word_pair, flip_timer 
    
    if flip_timer:
        window.after_cancel(flip_timer)
    
    word_pair = r.choice(data_dict)
    french_word = word_pair["French"]
    canvas.itemconfig(canvas_word, text=french_word)
    canvas.itemconfig(canvas_title, text="French")
    canvas.itemconfig(main_canvas, image=front_card_img)
    
    flip_timer= window.after(5000, flip_card, word_pair)
    

def handle_right_button_click():
    word_pair_to_remove = word_pair
    data_dict.remove(word_pair_to_remove)
    show_new_card()
    
def save_to_learn_words():
    df = pd.DataFrame(data_dict)
    df.to_csv("words_to_learn.csv", index=False)
    
    

    
def flip_card(word_pair):
    if word_pair:
        english_word = word_pair["English"]
        canvas.itemconfig(canvas_title, text="English")
        canvas.itemconfig(canvas_word, text=english_word)
        canvas.itemconfig(main_canvas, image=back_card_image)



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



# canvas object enables us to lay objects ontop of each other
canvas = Canvas(width=800, height=526)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
main_canvas = canvas.create_image(400, 265, image=front_card_img)
canvas_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="donne", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=show_new_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=handle_right_button_click)
right_button.grid(row=1, column=1)


show_new_card()

window.mainloop()
save_to_learn_words()