from tkinter import *
import pandas as pd
import os
from random import choice

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ------- Data ------- #
current_card = {}

try:
    # data = pd.read_csv("data/french_words.csv")
    data = pd.read_csv("data/words_to_learn.csv")
    data_list = data.to_dict(orient="records")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    data_list = data.to_dict(orient="records")


# ------- Saving progress ------- #


def remove_known_words():
    global data_list
    data_list.remove(current_card)
    new_data_list = pd.DataFrame(data_list)
    new_data_list.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ------- Card feats ------- #


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(data_list)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(display_card, image=fcard_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(lang_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=current_card["English"], fill="black")
    canvas.itemconfig(display_card, image=bcard_img)


# ------- UI ------- #
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)
# Card
fcard_img = PhotoImage(file="images/card_front.png")
bcard_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
display_card = canvas.create_image(400, 263, image=fcard_img)
# canvas.create_image(400, 263, image=bcard_img)
canvas.grid(row=0, column=0, columnspan=2)
lang_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
# Buttons
right_img = PhotoImage(file="images/right.png")
right_btn = Button(
    image=right_img,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    command=remove_known_words,
)
right_btn.grid(row=1, column=1)
wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(
    image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card
)
wrong_btn.grid(row=1, column=0)

next_card()

window.mainloop()
