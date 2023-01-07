from random import randint, choice

# from turtle import Turtle, Screen
import turtle as t


michael_the_big = t.Turtle()
michael_the_big.shape("turtle")

# michael_the_big.circle(100, 100, 100)
#
# michael_the_big.left(90)
# michael_the_big.forward(100)
# michael_the_big.left(90)
# michael_the_big.forward(100)
# michael_the_big.left(90)
# michael_the_big.forward(100)
# michael_the_big.left(90)
# michael_the_big.forward(100)


# for i in range(10):
#     michael_the_big.forward(10)
#     michael_the_big.penup()
#     michael_the_big.forward(10)
#     michael_the_big.pendown()


# for i in range(3, 9):
#     # print(i)
#     michael_the_big.pencolor(colors[i-3])
#     for j in range(i):
#         print(j)
#         michael_the_big.forward(100)
#         michael_the_big.right(360 / i)

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         michael_the_big.forward(100)
#         michael_the_big.right(angle)

# for shape_size_n in range(3,11):
#     michael_the_big.pencolor(choice(colors))
#     draw_shape(shape_size_n)

# while True:
#     random_move = randint(0, 3)
#     if random_move == 0:
#         michael_the_big.pencolor(choice(colors))
#         michael_the_big.forward(10)
#     elif random_move == 1:
#         michael_the_big.pencolor(choice(colors))
#         michael_the_big.right(90)
#         michael_the_big.forward(10)
#     elif random_move == 2:
#         michael_the_big.pencolor(choice(colors))
#         michael_the_big.left(90)
#         michael_the_big.forward(10)
#     else:
#         michael_the_big.pencolor(choice(colors))
#         michael_the_big.left(180)
#         michael_the_big.forward(10)
colors = ["red", "green", "blue", "orange", "purple", "brown", "yellow"]
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)
    # return f"rgb({r},{g},{b})"


colorRandomized = random_color()
print(colorRandomized)

directions = [0, 90, 180, 270]
michael_the_big.pensize(15)
michael_the_big.speed("fastest")

for _ in range(200):
    michael_the_big.color(random_color())
    michael_the_big.forward(30)
    michael_the_big.setheading(choice(directions))

screen = t.Screen()
screen.exitonclick()


# import heroes
# print(heroes.gen())
