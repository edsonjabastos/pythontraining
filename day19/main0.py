from turtle import Turtle, Screen

michael_the_big = Turtle()
michael_the_big.shape("turtle")
michael_the_big.speed("fastest")

screen = Screen()


def move_foward():
    michael_the_big.forward(10)


def move_backward():
    michael_the_big.backward(10)


def turn_left():
    new_heading = michael_the_big.heading() + 10
    michael_the_big.setheading(new_heading)


def turn_right():
    new_heading = michael_the_big.heading() - 10
    michael_the_big.setheading(new_heading)


def clear():
    michael_the_big.clear()
    michael_the_big.penup()
    michael_the_big.home()
    michael_the_big.pendown()


screen.listen()
screen.onkey(key='w', fun=move_foward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
