from tkinter import *
from tkinter import messagebox
import os
from random import randint, choice, shuffle
import pyperclip

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, "end")
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email_uname = email_uname_input.get()
    password = password_input.get()
    if website.strip() == "" or password.strip() == "":
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!"
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email_uname}\nPassword: {password}\nIs it ok to save?",
        )
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}  |  {email_uname}  |  {password}\n")
            website_input.delete(0, "end")
            password_input.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
# Screen
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# Image canvas
locker_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 95, image=locker_img)
canvas.grid(column=1, row=0)
# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_uname_label = Label(text="Email/Username:")
email_uname_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# Inputs
website_input = Entry(width=45)
website_input.grid(column=1, row=1, columnspan=2, sticky="Nsew")
website_input.focus()
email_uname_input = Entry(width=45)
email_uname_input.grid(column=1, row=2, columnspan=2, sticky="Nsew")
email_uname_input.insert(0, "edsonjabastos@hotmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="Nsew")
# Buttons
generate_pw_button = Button(text="Generate Password", command=generate_password)
generate_pw_button.grid(column=2, row=3, sticky="Nsew")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="Nsew")

window.mainloop()
