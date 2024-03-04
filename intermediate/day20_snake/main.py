# Import packages
from turtle import Screen
import time
import snake

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Niscient Snake")

# Create Snake
snake = snake.Snake()

# Set up screen listening, movement
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.2)

# Control the snake
# Up, down, left, right keys

screen.exitonclick()
