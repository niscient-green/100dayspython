# A game that asks the user to choose which person has more social media followers

# Import packages and data
import os
import day14_art
import day14_game_data
import random

# Display starting logo
print(day14_art.logo)

# Function: Choose a random person from data set
def choose_person():
    return random.choice(day14_game_data.data)

# Function: Display those persons and art
def display_persons(dct_person_A, dct_person_B):
    # print(lst_chosen_persons)
    print(f"Compare A: {dct_person_A["name"]}, {dct_person_A["description"]}, from {dct_person_A["country"]}")
    print(day14_art.vs)
    print(f"Against B: {dct_person_B["name"]}, {dct_person_B["description"]}, from {dct_person_B["country"]}")

# Function: Ask the user which person has more followers, return their choice
def ask_user_choice():
    chr_user_choice = input("Who has more followers? Type 'A' or 'B': ")
    return chr_user_choice

# Function: Check the user's answer, tell the user if they were right or wrong, return True if correct, False if wrong
def check_answer(dct_person_A, dct_person_B, chr_user_choice):
    if chr_user_choice == 'A':
        if dct_person_A["follower_count"] > dct_person_B["follower_count"]:
            return True
        else:
            return False
    else:
        if dct_person_A["follower_count"] < dct_person_B["follower_count"]:
            return True
        else:
            return False

# Function: Play the game, return True if user was correct
def play_game():
    display_persons(dct_person_A, dct_person_B)
    chr_user_choice = ask_user_choice()
    return check_answer(dct_person_A, dct_person_B, chr_user_choice)

# Main loop
# Initialize first round
int_score = 0
boo_continue = True
dct_person_A = choose_person()
dct_person_B = choose_person()

while boo_continue:
    # If selected the same persons, choose different random person B
    while dct_person_A == dct_person_B:
        dct_person_B = choose_person()
    
    if play_game():
        os.system('cls')
        # If they were right, select and display another choice
        int_score += 1
        print(f"You're right! Current score: {int_score}.")
        dct_person_A = dct_person_B
        dct_person_B = choose_person()
    else:
        # If they were wrong, display the user's final score and exit
        print(f"Wrong. Sad. Final score: {int_score}.")
        boo_continue = False
