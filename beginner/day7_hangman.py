# import libraries
import random
import day7_hangman_art
import day7_hangman_words
import os

# set up
int_lives_remaining = 6
lst_guesses = []

# chose a word randomly
chosen_word = random.choice(day7_hangman_words.lst_words)
print(f"Pssst. The chosen word is {chosen_word}")
int_solution_length = len(chosen_word)

# create blank solution string
lst_solution = []
for _ in chosen_word:
    lst_solution.append("_")
print(lst_solution)

# loop to ask user for guess, check guess, check if won or lost
boo_end_of_game = False
print(day7_hangman_art.str_logo)

while not boo_end_of_game:
    # ask user to guess letter
    guess = input("Guess a letter: ").lower()
    if guess in lst_guesses:
      print("You've already guess that.")
    else:
      lst_guesses.append(guess)

      # check if guess is correct
      for int_current_position in range(int_solution_length):
          chr_letter = chosen_word[int_current_position]
          if (guess == chr_letter):
              boo_found_guess = True
              lst_solution[int_current_position] = guess
      
      # tell use if guess was correct
      if guess in chosen_word:
          print("Correct guess!")
      
      # if all letters guessed, win the game
      if "_" not in lst_solution:
          print("You win!")
          boo_end_of_game = True
      
      # if guess was not found anywhere, lose a life
      if guess not in chosen_word:
          print("Wrong! Uh oh.")
          int_lives_remaining -= 1
          if int_lives_remaining == 0:
              print("You lose. You're dead. Nice job.")
              boo_end_of_game = True
w
    
    # print the current stage 
    print(day7_hangman_art.lst_stages[int_lives_remaining])
            
    # join all the elements in the list and turn it into a String.
    print(f"{' '.join(lst_solution)}\n")