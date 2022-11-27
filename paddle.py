from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coords):
        super().__init__("square")
        self.position_paddle(coords)

    def position_paddle(self, coords):
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.shapesize(5, 1, None)
        self.goto(coords)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
