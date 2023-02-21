from tkinter import *

# import turtle
#
window = Tk()
window.title("Mile to KM Converter")
# window.minsize(width=100, height=100)
window.config(padx=50, pady=50)
# Labels
mile_label = Label(text="Mile(s)")
mile_label.grid(column=2, row=0)
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
km_label = Label(text="0")
km_label.grid(column=1, row=1)
km_unit_label = Label(text="KM")
km_unit_label.grid(column=2, row=1)


def mile_to_km():
    miles = float(input.get())
    km = miles * 1.609
    km_label["text"] = round(km, 2)

# Button
button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()
