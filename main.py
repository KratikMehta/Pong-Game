from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

right_paddle = Paddle("right")
left_paddle = Paddle("left")
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(fun=right_paddle.up, key="Up")
screen.onkeypress(fun=right_paddle.down, key="Down")

screen.onkeypress(fun=left_paddle.up, key="w")
screen.onkeypress(fun=left_paddle.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Detect collision with top and bottom wall.
    ball.bounce_y()
    # Detect collision with right wall.
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()
    # Detect collision with left wall.
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()
    # Detect collision with paddle.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.moving_distance += 1
        ball.bounce_x()
    ball.move_ball()

screen.exitonclick()
