# Create ball class (display, move, score)

# Import packages
from turtle import Turtle
import globals as g
import random
import time


# Ball class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.resizemode("user")
        self.shapesize(stretch_wid=g.BALL_STRETCH, stretch_len=g.BALL_STRETCH)
        self.color(g.SCREEN_FG)
        self.penup()
        self.starting_position()

    # Move ball back to home
    def starting_position(self):
        self.goto(0, 0)
        # Start in random part of 90 degree cone facing player1
        start_heading = random.randint(0, 90) + 135
        # start_heading = 45
        self.setheading(start_heading)

    def move(self):
        self.wall_collision()
        self.forward(g.BALL_MOVE)

    # Check if ball hits top or bottom wall
    def wall_collision(self):
        if (self.ycor() > ((g.SCREEN_HEIGHT / 2) - g.SCREEN_PADDING) or
                self.ycor() < -((g.SCREEN_HEIGHT / 2) - g.SCREEN_PADDING)):
            current_heading = self.heading()
            new_heading = (360 - current_heading) % 360
            self.setheading(new_heading)

    # Checks for boundary and paddle collision
    def boundary_collision(self, player1, player2):
        current_heading = self.heading()

        # Check if near left boundary
        if self.xcor() < -((g.SCREEN_WIDTH / 2) - g.BALL_PADDING):
            # Check for player1 paddle
            if (player1.ycor() - + g.PADDLE_HEIGHT / 2) < self.ycor() < (player1.ycor() + g.PADDLE_HEIGHT / 2):
                new_heading = (180 - current_heading) % 360
                self.setheading(new_heading)
            else:
                self.score_point(player2)

        # Check if near right boundary
        elif self.xcor() > ((g.SCREEN_WIDTH / 2) - g.BALL_PADDING):
            # Check for player2 paddle
            if (player2.ycor() - + g.PADDLE_HEIGHT / 2) < self.ycor() < (player2.ycor() + g.PADDLE_HEIGHT / 2):
                new_heading = (180 - current_heading) % 360
                self.setheading(new_heading)
            else:
                self.score_point(player1)

    # Increase score, reset ball
    def score_point(self, player):
        player.increase_score()
        self.starting_position()
        time.sleep(2)
