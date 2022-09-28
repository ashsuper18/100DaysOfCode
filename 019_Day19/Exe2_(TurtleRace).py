from turtle import Turtle, Screen, color, screensize
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colorlist = ["red", "green", "yellow", "blue", "black"]
y_axis = [-70, -40, -10, 20, 50]
user_guess = screen.textinput("Hello", "Place your bet:")
all_turtle = []
# screen.bgpic("019_Day19//racetrack.png")

for i in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colorlist[i])
    new_turtle.penup()
    new_turtle.speed(0)
    new_turtle.goto(-230, y_axis[i])
    all_turtle.append(new_turtle)

if user_guess:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            wining_turtle = turtle.pencolor()
            if wining_turtle == user_guess:
                print("You won the Bet")
            else:
                print("Try Again")
            is_race_on = False
        ran_distance = random.randint(0, 10)
        turtle.forward(ran_distance)


screen.exitonclick()
