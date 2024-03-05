from turtle import Turtle
import globals as g


# Draw the dotted midline down the screen
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
