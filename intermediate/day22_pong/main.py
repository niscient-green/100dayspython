# Recreate the game of Pong
# Import packages
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Set globals
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 1000
SCREEN_BG = "black"

# Create paddles, ball, scoreboard
left_paddle = Paddle()
right_paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

# TODO: Create game screen (display)
# Set up screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BG)
screen.tracer(0)
screen.title("Niscient Pong")

# Set up screen listening, movement
# Keys are set up for Niscient Colemak layout
# TODO: change to left, right paddles
screen.listen()
# Left paddle
screen.onkey(key="f", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)
# Right paddle
screen.onkey(key="u", fun=right_paddle.up)
screen.onkey(key="e", fun=right_paddle.down)
# TODO: Write quit function
screen.onkey(key="q", fun=scoreboard.quit)

# Main game loop
game_is_on = True
while game_is_on:
    scoreboard.display()
    # TODO: Determine win condition (first to reach 10)


screen.exitonclick()
