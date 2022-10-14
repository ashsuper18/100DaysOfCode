from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, postion):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(postion)
        self.left(90)

    def move_up(self):
        self.fd(30)


    def move_down(self):
        self.backward(30)
