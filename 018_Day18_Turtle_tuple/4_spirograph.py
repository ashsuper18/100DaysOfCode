from turtle import Screen, Turtle
import random

tim = Turtle()
tim.speed("fastest")
tim.pensize(3)


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)


for i in range(360):
    change_color()
    tim.circle(100)
    tim.setheading(i)


screen = Screen()
screen.exitonclick()
