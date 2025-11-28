from tkinter import *
import math
import winsound
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
DURATION_MS = 10000
reps = 0
timer = None


def play_sound(duration_ms):
    # Play the sound asynchronously (non-blocking)
    winsound.PlaySound("alarm.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

    # Convert ms → seconds
    time.sleep(duration_ms / 1000)

    # Stop the sound
    winsound.PlaySound(None, winsound.SND_PURGE)

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    # stops the current running timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        # time for long break
        play_sound(DURATION_MS)
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        # time for short break
        play_sound(DURATION_MS)
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        if reps > 1:
            play_sound(DURATION_MS)
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    
    # change the text in the canvas to reflect current remaining time
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}") 
    if count > 0:
        global timer
        timer =  window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range( work_sessions):
            check_mark += "✔️"
        check_marks.config(text=check_mark)
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=200, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(40))
check_marks.grid(column=1, row=3)


window.mainloop()