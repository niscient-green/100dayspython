# Tracks the user's score

# Import packages
from turtle import Turtle

# Set globals
ALIGNMENT = "center"
FONT = ("Roman", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.color("white")
        self.speed("fastest")

    def display(self):
        self.clear()
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.display()
