from turtle import  Screen
from ball import Ball
from paddles import Paddle
from scoreboard import Scoreboard
import time


screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
# 
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update( )
    ball.move()
    # Detect collison with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # detect collison with board
    if ball.distance(r_paddle) < 50 and ball.xcor() >330:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() <-330:
        ball.bounce_x()

    # ball pass the screen
    if ball.xcor() > 380:
        ball.reset_postion()
        scoreboard.l_point()

    if ball.xcor() <-380:
        ball.reset_postion()
        scoreboard.r_point()


screen.exitonclick()
