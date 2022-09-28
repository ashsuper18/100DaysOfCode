from turtle import Turtle, Screen, clear

tim = Turtle()
screen = Screen()

# NOTES try to use keywords argument in methods which we have created by ourself means try give names like function and key what you are writing.


def move_forwards():
    tim.forward(25)


def move_backwards():
    tim.backward(25)


def move_counter_clockwise():
    new_heading = tim.heading() - 15
    tim.setheading(new_heading)


def move_counter_anticlockwise():
    tim.left(15)


def reset():
    tim.reset()


screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_counter_anticlockwise, key="a")
screen.onkey(fun=move_counter_clockwise, key="d")
screen.onkey(fun=reset, key="c")
screen.listen()
screen.exitonclick()
