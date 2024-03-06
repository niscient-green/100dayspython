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
        self.forward(c.TURTLE_MOVE)

    # Turtle moves down
    def down(self):
        self.backward(c.TURTLE_MOVE)
