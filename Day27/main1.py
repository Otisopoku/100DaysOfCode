import tkinter
window = tkinter.Tk()

window.title("GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

#Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="Another new text")
my_label.grid(column=0, row=0) # without this function, we can't see anything on our screen


num_of_clicks = 0

def button_clicked():
    input_string = input.get()
    my_label["text"] = input_string
    

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=1)

#Entry

input = tkinter.Entry(width=20)
input.grid(column=2,row=2)

window.mainloop()
    