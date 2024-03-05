# Recreate the game of Pong
# Import packages
from turtle import Turtle, Screen
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


def draw_midline():
    midline = Turtle()
    midline.hideturtle()
    midline.pencolor(g.SCREEN_FG)
    midline.penup()
    midline.goto(x=0, y=g.SCREEN_HEIGHT / 2)
    midline.pendown()
    midline.setheading(g.SOUTH)
    num_midline = int(g.SCREEN_HEIGHT / (g.MIDLINE_LEN + g.MIDLINE_SPACE)) + 1
    for _ in range(0, num_midline):
        midline.forward(g.MIDLINE_LEN)
        midline.penup()
        midline.forward(g.MIDLINE_SPACE)
        midline.pendown()


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
    scoreboard.display()
    screen.update()
    time.sleep(0.2)

    # TODO: Test win condition
    # Determine win condition (first to reach WINNING_SCORE)
    if scoreboard.left_score == g.WINNING_SCORE:
        scoreboard.game_over("Left Player")
        game_is_on = False
    elif scoreboard.right_score == g.WINNING_SCORE:
        scoreboard.game_over("Right Player")
        game_is_on = False

screen.exitonclick()
