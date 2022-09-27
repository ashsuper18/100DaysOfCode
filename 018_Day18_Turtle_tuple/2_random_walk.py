import random
from turtle import Screen, Turtle

timmy = Turtle()


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)


direction = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed("fastest")


for _ in range(200):
    change_color()
    timmy.forward(random.randint(10, 50))
    timmy.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()
