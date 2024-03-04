# Import packages
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set globals
WALL = 280

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Niscient Snake")

# Create Snake, Food, Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up screen listening, movement
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    snake.move()
    scoreboard.display()
    screen.update()
    time.sleep(0.2)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.move()
        scoreboard.increase()
        snake.new_segment()

    # Detect collision with wall
    if snake.head.xcor() > WALL or snake.head.xcor() < -WALL or snake.head.ycor() > WALL or snake.head.ycor() < -WALL:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    if snake.is_collided():
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
