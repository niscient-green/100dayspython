from turtle import Turtle, Screen
import random

# Create the turtle racers
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
for color in colors:
    new_turtle = Turtle()
    new_turtle.color(color)
    all_turtles.append(new_turtle)


# Move turtle forward by amount
def move_forward(current_turtle, amount):
    current_turtle.forward(amount)


# Set up screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

# Ask user for bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race (enter a color)? ")
print(user_bet)

# Set up all turtles
for current_turtle in all_turtles:
    current_turtle.penup()
    current_turtle.shape("turtle")

# Set starting positions of turtles
number_of_turtles = len(all_turtles)
current_turtle_number = 1
for current_turtle in all_turtles:
    starting_x = -1 * SCREEN_WIDTH / 2 + 50
    starting_y = (current_turtle_number * (SCREEN_HEIGHT - 50) / number_of_turtles) - SCREEN_HEIGHT / 2
    current_turtle.goto(x=starting_x, y=starting_y)
    current_turtle_number += 1

# Main program loop
is_race_on = True
while is_race_on:
    # Move all the turtles forward
    for current_turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        move_forward(current_turtle, rand_distance)

    # Check if any turtle has crossed finish line
    for current_turtle in all_turtles:
        if current_turtle.position()[0] > (SCREEN_WIDTH / 2 - 50):
            is_race_on = False
            winning_color = current_turtle.color()[0]
            print(f"The {winning_color} turtle won.")
            if user_bet == winning_color:
                print("You guessed the winner correctly!")
            else:
                print("You bet wrong. Sorry.")
            break

screen.exitonclick()
