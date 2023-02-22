from tkinter import *
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email_uname = email_uname_input.get()
    password = password_input.get()
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
generate_pw_button = Button(text="Generate Password")
generate_pw_button.grid(column=2, row=3, sticky="Nsew")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="Nsew")

window.mainloop()
