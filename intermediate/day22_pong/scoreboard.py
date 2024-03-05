# Import packages
from turtle import Turtle

# Set globals
ALIGNMENT = "center"
FONT = ("Courier", 36, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=(500/2 - 50))
        self.speed("fastest")

    def display(self):
        self.clear()
        self.write(arg=f"{self.left_score}    {self.right_score}", align=ALIGNMENT, font=FONT)

    def increase(self, player):
        if player == "left":
            self.left_score += 1
        elif player == "right":
            self.right_score += 1
        else:
            print("ERROR: incorrect player specified.")

    def game_over(self, winner):
        self.goto(x=0, y=0)
        self.write(arg=f"{winner} wins!", align=ALIGNMENT, font=FONT)
