from random import randint, choice
from turtle import Turtle, Screen


michael_the_big = Turtle()
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


colors = ["red", "green", "blue", "orange", "purple", "brown", "yellow"]
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

# screen = Screen()
# screen.exitonclick()


# import heroes
# print(heroes.gen())
