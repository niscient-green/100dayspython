# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import day12_art
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Show welcome
print(day12_art.logo)
print("Welcome to the Number Guessing Game!")

def compare_guess(guess, answer):
    if guess < answer:
        print("Too low.")
        return 0
    if guess > answer:
        print("Too high.")
        return 1
    else:
        print("Spot on!")
        return 2

def guess(guesses_remaining, answer):
    guessed_correctly = False
    # While guesses remain and user has not guessed correctly, run this loop
    while guesses_remaining > 0 and guessed_correctly == False:
        # Ask user for their guess
        print(f"You have {guesses_remaining} guesses remaining.")
        guess = int(input("Make a guess: "))
        guesses_remaining -= 1

        # Check guess against answer, inform user if too high, low, or correct
        if compare_guess(guess, answer) == 2:
            guessed_correctly = True
            return 1
    
    return 0

def play_game():    
    # Choose an answer
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randrange(1, 101)
    # Debug cheat
    print(f"Psssst. The answer is {answer}.")

    # Have user choose a difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        guesses_remaining = EASY_LEVEL_TURNS
    else:
        guesses_remaining = HARD_LEVEL_TURNS
    
    end_game = guess(guesses_remaining, answer)
    if end_game == 0:
        print("You lose. Sad.")
    else:
        print("You win!")


# Main program loop
play_game()
