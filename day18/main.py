from random import randint, choice

# from turtle import Turtle, Screen
import turtle as t


michael_the_big = t.Turtle()
michael_the_big.shape("turtle")
michael_the_big.speed("fastest")

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
# colors = ["red", "green", "blue", "orange", "purple", "brown", "yellow"]
t.colormode(255)

screen = t.Screen()
screen.bgcolor("black")

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color
    # return f"rgb({r},{g},{b})"
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        michael_the_big.color(random_color())
        michael_the_big.circle(100)
        michael_the_big.setheading(michael_the_big.heading() + size_of_gap)

draw_spirograph(2)

# colorRandomized = random_color()
# print(colorRandomized)

# directions = [0, 90, 180, 270]
# michael_the_big.pensize(15)

# for _ in range(200):
#     michael_the_big.color(random_color())
#     michael_the_big.forward(30)
#     michael_the_big.setheading(choice(directions))



# for i in range(6):

#       # Choose your color combination
#     for color in ('red', 'magenta', 'blue',
#                   'cyan', 'green', 'white',
#                   'yellow'):
#         michael_the_big.color(color)

#         # Draw a circle of chosen size, 100 here
#         michael_the_big.circle(100)

#         # Move 10 pixels left to draw another circle
#         michael_the_big.left(10)


screen.exitonclick()
# import heroes
# print(heroes.gen())
