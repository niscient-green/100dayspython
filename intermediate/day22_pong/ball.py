# TODO: Create ball class (display, move, score)

# Import packages
from turtle import Turtle
import globals as g


# Ball class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_wid=g.BALL_STRETCH, stretch_len=g.BALL_STRETCH)
        self.color(g.SCREEN_FG)
        self.penup()
