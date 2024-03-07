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
        # Get high score from file
        with open("high_score.txt") as score_file:
            self.high_score = int(score_file.read())
            score_file.close()
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

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as score_file:
                score_file.write(str(self.high_score))
                score_file.close()

        self.score = 0
        self.display()
