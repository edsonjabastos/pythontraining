from tkinter import *

# import turtle
#
window = Tk()
window.title("my First GUI Program")
window.minsize(width=500, height=300)
# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()


# my_label["text"] = "oioi"
# my_label.config(text="oioioi")

# Button
def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()


button = Button(text="Click me!", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()

window.mainloop()

# tim = turtle.Turtle()
# tim.write("oi")

# def add(*args):
#     print(args)
#     print(type(args))
#     acc = 0
#     for n in args:
#         acc += n
#     return acc
#
#
# print(add(24, 26, 25, 25))


# def calculate(n, **kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     # n += kwargs.add    #NÃO FUNCIONA
#     # n *= kwargs.multiply
#     print(n)
#
#
# calculate(2, add=3, multiply=5)
# calculate(eita="eitanós", epa="epanóis")

# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.colour = kw.get("colour")
#         self.seats = kw.get("seats")
#
#
# my_car = Car(make="Nissan")
#
# print(my_car.model)
# print((my_car))