from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if self.side.lower() == "right":
            self.goto(350, 0)
        elif self.side.lower() == "left":
            self.goto(-350, 0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
