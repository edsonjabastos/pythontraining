from another_package import another_package_variable
print(another_package_variable)

from turtle import Turtle, Screen

tommy = Turtle()
tommy.shape("turtle")
tommy.color("green")
tommy.fd(300)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

