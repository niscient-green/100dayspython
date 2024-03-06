# Import packages
from turtle import Turtle
import config as c


# Track and display the player's level
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=-c.SCREEN_WIDTH_PAD, y=c.SCREEN_HEIGHT_PAD - 20)
        self.speed("fastest")

    # Display the level
    def display(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align=c.LEVEL_ALIGN, font=c.LEVEL_FONT)

    # Display end game message
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align=c.END_MSG_ALIGN, font=c.END_MSG_FONT)

    # Increase the level
    def level_up(self):
        self.level += 1
