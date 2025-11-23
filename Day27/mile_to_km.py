from tkinter import *
import math

window = Tk()

def calculate():
    res = miles_entry.get().strip()
    res = int(res)
    result = round((res * 1.609344), 2)
    converted_label.config(text=str(result))
    

equal_to_label = Label(text="is equal to", font=("Arial", 14, "normal"))
equal_to_label.grid(column=0, row=1)

miles_entry = Entry()
miles_entry.grid(column=1, row=0)

miles_text = Label(text="Miles", font=("Arial", 14, "normal"))
miles_text.grid(column=2, row=0)

converted_label = Label(text="0", font=("Arial", 14, "normal"))
converted_label.grid(column=1, row=1)

km_text = Label(text="Km", font=("Arial", 14, "normal"))
km_text.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)

window.title("Mile to Km Converter")
window.config(padx=50, pady=50)
window.minsize(width=300, height=400)
window.mainloop()
