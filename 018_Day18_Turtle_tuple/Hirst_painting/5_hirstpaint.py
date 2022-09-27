#
#! Extract  colors from an image.
# import colorgram
# colors = colorgram.extract(
#     '018_Day18_Turtle_tuple\Hirst_painting\sample.jpg', 100)
# first_color = colors[0]
# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_list.append((r, g, b))
# print(rgb_list)

import random
import turtle as tutle

tutle.colormode(255)
color_list = [(28, 37, 55), (226, 232, 242), (236, 154, 96), (229, 215, 86), (132, 165, 204), (244, 240, 242), (244, 246, 244), (202, 135, 144), (155, 29, 27), (197, 55, 35), (19, 105, 162), (123, 72, 79), (174, 184, 218), (171, 27, 30), (233,
                                                                                                                                                                                                                                               166, 171), (57, 45, 42), (135, 191, 166), (18, 56, 53), (34, 29, 35), (20, 63, 125), (32, 78, 91), (240, 154, 151), (177, 100, 104), (197, 90, 77), (113, 125, 147), (74, 103, 102), (171, 203, 192), (64, 144, 185), (42, 77, 75), (170, 198, 210)]

tim = tutle.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(25, random.choice(color_list))
    tim.penup()
    tim.forward(40)
    tim.pendown()
    if dot_count % 10 == 0:
        tim.penup()
        tim.left(90)
        tim.forward(40)
        tim.left(90)
        tim.forward(400)
        tim.setheading(0)


screen = tutle.Screen()
screen.exitonclick()
