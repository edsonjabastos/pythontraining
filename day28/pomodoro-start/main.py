import math
from tkinter import *
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break.", fg=RED)
    # If it's 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break.", fg=PINK)
    # If it's the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        title.config(text="Work!", fg=GREEN)

    # count_down(10)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # check_mark = "✔"
        # if reps % 2 == 0:
        #     checks_qty = int(reps / 2)
        #     check_marks = checks_qty * check_mark
        #     check.config(text=check_marks) #mine solution (works!)
        marks = ''
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text=marks)  # mine solution (works!)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
# Timer
canvas = Canvas(width=202, height=230, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 115, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)
# Labels
title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
title.grid(column=1, row=0)
check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)
# Buttons
start_btn = Button(text="Start", command=start_timer, highlightthickness=0)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_btn.grid(column=2, row=2)
window.mainloop()
