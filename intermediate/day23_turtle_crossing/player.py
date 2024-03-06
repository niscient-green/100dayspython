# Player turtle class (move up, move down)
from turtle import Turtle
import config as c


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color(c.SCREEN_FG)
        self.setheading(c.NORTH)
        self.goto(c.TURTLE_START)

    # Turtle moves up
    def up(self):
        if self.ycor() < c.SCREEN_HEIGHT_PAD:
            self.forward(c.TURTLE_MOVE)

    # Turtle moves down
    def down(self):
        if self.ycor() > -c.SCREEN_HEIGHT_PAD:
            self.backward(c.TURTLE_MOVE)

    # todo: Increase the level, reset position
    def level_up(self):
        self.goto(c.TURTLE_START)

    # Check if player reaches finish line
    def check_finish(self):
        if self.ycor() > (c.SCREEN_HEIGHT_PAD - 40):
            return True
        else:
            return False
