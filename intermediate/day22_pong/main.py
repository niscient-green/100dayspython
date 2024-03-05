# Recreate the game of Pong
# Import packages
from turtle import Screen
from midline import draw_midline
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import globals as g
import time

game_is_on = True

# Set up screen
screen = Screen()
screen.setup(width=g.SCREEN_WIDTH, height=g.SCREEN_HEIGHT)
screen.bgcolor(g.SCREEN_BG)
screen.tracer(0)
screen.title("Niscient Pong")
screen.register_shape(name="paddle", shape=(
    (-g.PADDLE_WIDTH / 2, g.PADDLE_HEIGHT / 2), (g.PADDLE_WIDTH / 2, g.PADDLE_HEIGHT / 2),
    (g.PADDLE_WIDTH / 2, -g.PADDLE_HEIGHT / 2), (-g.PADDLE_WIDTH / 2, -g.PADDLE_HEIGHT / 2)))


# Create paddles, ball, scoreboard, screen
player1 = Paddle(g.PLAYER1)
player2 = Paddle(g.PLAYER2)
ball = Ball()
scoreboard = Scoreboard()

# Set up screen listening, movement
# Keys are set up for Niscient Colemak layout
screen.listen()
if g.KEYMAP == "colemak":
    # Left paddle
    screen.onkey(key="f", fun=player1.up)
    screen.onkey(key="s", fun=player1.down)
    # Right paddle
    screen.onkey(key="u", fun=player2.up)
    screen.onkey(key="e", fun=player2.down)
else:
    # Left paddle
    screen.onkey(key="w", fun=player1.up)
    screen.onkey(key="s", fun=player1.down)
    # Right paddle
    screen.onkey(key="e", fun=player2.up)
    screen.onkey(key="k", fun=player2.down)

# Draw midline
draw_midline()

# Main game loop
while game_is_on:
    scoreboard.display(player1=player1, player2=player2)
    ball.move()
    screen.update()
    time.sleep(g.REFRESH)

    # Test scoring condition
    ball.boundary_collision(player1=player1, player2=player2)

    # Test win condition
    if player1.score == g.WINNING_SCORE:
        scoreboard.game_over(player1)
        game_is_on = False
    elif player2.score == g.WINNING_SCORE:
        scoreboard.game_over(player2)
        game_is_on = False

screen.exitonclick()
