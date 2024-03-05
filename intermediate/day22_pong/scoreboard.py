# Import packages
from turtle import Turtle

# Set globals
ALIGNMENT = "center"
FONT = ("Courier", 36, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=(500/2 - 50))
        self.speed("fastest")

    # Display the score
    def display(self, player1, player2):
        self.clear()
        self.write(arg=f"{player1.score}    {player2.score}", align=ALIGNMENT, font=FONT)

    # Display end game message
    def game_over(self, player):
        self.goto(x=0, y=0)
        self.write(arg=f"{player.name} wins!", align=ALIGNMENT, font=FONT)
