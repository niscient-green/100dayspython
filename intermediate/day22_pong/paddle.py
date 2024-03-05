# Paddle class (display, move)

# Import packages
from turtle import Turtle
import globals as g


# Paddle class
class Paddle(Turtle):
    def __init__(self, player_side):
        super().__init__()
        self.shape("paddle")
        self.color(g.SCREEN_FG)
        self.penup()
        self.initial_position(player_side)

    # Set each player's initial position
    def initial_position(self, player_side):
        position_multiplier = 1
        if player_side == g.PLAYER1:
            position_multiplier = -1
        self.setheading(g.NORTH)
        self.goto(x=(g.SCREEN_WIDTH / 2 - g.PADDLE_WIDTH * 2) * position_multiplier, y=0)

    # Move paddle up
    def up(self):
        self.clear()
        self.setheading(g.NORTH)
        self.forward(g.MOVE_DISTANCE)

    # Move paddle down
    def down(self):
        self.clear()
        self.setheading(g.SOUTH)
        self.forward(g.MOVE_DISTANCE)
