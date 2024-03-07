# Recreate the game of Frogger as Turtler

# Import packages
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import config as c
import time

game_is_on = True

# Set up screen
screen = Screen()
screen.setup(width=c.SCREEN_WIDTH, height=c.SCREEN_HEIGHT)
screen.bgcolor(c.SCREEN_BG)
screen.tracer(0)
screen.title("Niscient Turtler")

# Create player, cars, scoreboard
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Set up screen listening, movement
screen.listen()
screen.onkey(key="Up", fun=player.up)
screen.onkey(key="Down", fun=player.down)

# Main game loop
while game_is_on:
    # Update score board and move all cars
    scoreboard.display()
    cars.move_all_cars()

    # Check if player crossed finish line
    if player.check_finish():
        cars.level_up()
        player.level_up()
        scoreboard.level_up()

    # Check for game over
    if cars.check_collision(player):
        game_is_on = False
        scoreboard.game_over()

    # Update screen and wait
    screen.update()
    time.sleep(c.REFRESH)

screen.exitonclick()
