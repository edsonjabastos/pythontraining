# import colorgram
# colors = colorgram.extract('rayquaza.jpg', 50)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
import turtle as t
import random

t.colormode(255)
screen = t.Screen()
michael = t.Turtle()
michael.speed("fastest")
michael.hideturtle()
michael.penup()

rgb_colors = [(197, 162, 128), (242, 225, 177), (135, 157, 193), (77, 87, 131), (41, 38, 62), (96, 116, 177),
              (227, 210, 121), (46, 34, 45), (171, 150, 160), (112, 102, 64), (110, 82, 98), (68, 116, 64),
              (55, 53, 90), (190, 213, 232), (148, 155, 61), (143, 178, 133), (48, 39, 25), (172, 182, 218),
              (206, 223, 211), (101, 152, 81), (185, 105, 88), (79, 52, 73), (163, 107, 121), (75, 77, 33),
              (30, 49, 31), (42, 81, 43), (221, 207, 215), (229, 178, 161), (173, 206, 164), (206, 182, 192),
              (88, 52, 47), (217, 219, 8), (166, 200, 212), (102, 137, 143), (43, 74, 82)]

michael.setheading(225)
michael.forward(300)
michael.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    michael.dot(20, random.choice(rgb_colors))
    michael.forward(50)

    if dot_count % 10 == 0:
        michael.setheading(90)
        michael.forward(50)
        michael.setheading(180)
        michael.forward(500)
        michael.setheading(0)

screen.exitonclick()
