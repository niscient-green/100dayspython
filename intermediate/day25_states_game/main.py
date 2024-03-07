import turtle
import pandas

# Set constants
BG_IMAGE = "blank_states_img.gif"
FONT = "Courier"
FONT_ALIGN = "center"
FONT_TYPE = "normal"
FONT_SIZE = 10

# Set up screen
screen = turtle.Screen()
screen.title("Niscient US States Game")
screen.addshape(BG_IMAGE)

# Create background image
turtle.shape(BG_IMAGE)

# Create states and answer lists
answers = []
states_on_screen = []
states_df = pandas.read_csv("50_states.csv")

# Ask user for a guess
continue_game = True


# Check validity of guess
def check_guess(state_guess_title):
    # Check if answer has already been guessed
    if state_guess_title in answers:
        print("Already guessed!")
        return True
    # Check if guess is valid
    elif states_df.state.eq(state_guess_title).any():
        answers.append(state_guess_title)
        print("That's a new guess.")
        add_state_on_screen(state_guess_title)
        return True
    # Otherwise, quit game
    else:
        print("Bad guess.")
        return True


# For a valid guess, write text on the map
def add_state_on_screen(state_guess_title):
    new_state_turtle = turtle.Turtle()
    new_state_turtle.penup()
    new_state_turtle.hideturtle()
    # Find coordinates for this state
    x_cor = states_df[states_df.state == state_guess_title].x.item()
    y_cor = states_df[states_df.state == state_guess_title].y.item()
    new_state_turtle.goto(x_cor, y_cor)
    new_state_turtle.write(state_guess_title, align=FONT_ALIGN, font=(FONT, FONT_SIZE, FONT_TYPE))


# Main game loop
while continue_game:
    state_guess = screen.textinput(title=f"{len(answers)} / 50 States Correct", prompt="What is another state name?")
    state_guess_title = state_guess.title()
    continue_game = check_guess(state_guess_title)
    if len(answers) == 50:
        print("You win!")
        continue_game = False

screen.exitonclick()
