# Import packages
import turtle
from turtle import Turtle, Screen
import random

# Initialize the turtle
tim = Turtle()
# tim.shape("circle")
colors = ["SlateBlue", "DarkGreen", "DeepSkyBlue4", "navy", "MidnightBlue"]
turtle.colormode(255)


# # Make a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# # Make a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# # Make triangle through decagon
# for n in range(3, 11):
#     tim.color(random.choice(colors))
#     for i in range(0, n):
#         tim.forward(100)
#         tim.right(360 / n)

# Create and return random rgb tuple
def random_color():
    r = random.randint(0, 50)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# # Do a random walk
# tim.pensize(8)
# tim.speed("fastest")
# for _ in range(1000):
#     tim.pencolor(random_color())
#     tim.setheading(random.randint(0, 3) * 90)
#     tim.forward(30)


# Create a spirograph
tim.pensize(2)
tim.speed("fastest")
heading = 0
# Draw many circles
for _ in range(36):
    tim.pencolor(random_color())
    heading += 10
    tim.setheading(heading)
    # Draw a circle
    tim.circle(100)


# Build screen, set attributes
screen = Screen()
screen.exitonclick()
