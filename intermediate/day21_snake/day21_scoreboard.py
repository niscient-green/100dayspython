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
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=280)
        self.speed("fastest")

    def display(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game over.", align=ALIGNMENT, font=FONT)