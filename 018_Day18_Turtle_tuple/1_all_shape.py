import random
from turtle import Screen, Turtle

timmy = Turtle()


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.pencolor(R, G, B)
    timmy.color(R, G, B)


timmy.shape("triangle")
timmy.color("red")
for i in range(3, 11):
    change_color()
    for _ in range(i):
        timmy.speed(speed="fast")
        timmy.forward(100)
        timmy.right(360/i)


screen = Screen()
screen.exitonclick()
