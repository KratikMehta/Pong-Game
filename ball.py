from turtle import Turtle
import random

INITIAL_ANGLE = [45, 135, 225, 315]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.moving_distance = 10
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.choice(INITIAL_ANGLE))

    def move_ball(self):
        self.forward(self.moving_distance)

    def bounce_y(self):
        if (self.ycor() > 280 and self.xcor() > 0) or (self.ycor() < -280 and self.xcor() < 0):
            self.setheading(self.heading() - 90)
        elif (self.ycor() < -280 and self.xcor() > 0) or (self.ycor() > 280 and self.xcor() < 0):
            self.setheading(self.heading() + 90)

    def bounce_x(self):
        if self.heading() in [45, 225]:
            self.setheading(self.heading() + 90)
        elif self.heading() in [135, 315]:
            self.setheading(self.heading() - 90)

    def reset_ball(self):
        self.goto(0, 0)
        self.setheading(180 - self.heading())
        self.moving_distance = 10
