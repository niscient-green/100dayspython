# TODO: Create scoreboard class (display, update)

# Import packages
from turtle import Turtle
from main import SCREEN_WIDTH, SCREEN_HEIGHT

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
        self.goto(x=0, y=(SCREEN_HEIGHT/2 - 20))
        self.speed("fastest")

    def display(self):
        self.clear()
        self.write(arg=f"Score: {self.left_score} vs {self.right_score}", align=ALIGNMENT, font=FONT)

    def increase(self, player):
        if player == "left":
            self.left_score += 1
        elif player == "right":
            self.right_score += 1
        else:
            print("ERROR: incorrect player specified.")


    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game over.", align=ALIGNMENT, font=FONT)
