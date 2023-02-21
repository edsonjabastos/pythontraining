from tkinter import *

# import turtle
#
window = Tk()
window.title("my First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)
# Button
button = Button(text="Click me!")
button.grid(column=1, row=1)

# New Button
new_button = Button(text="Click me!")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
