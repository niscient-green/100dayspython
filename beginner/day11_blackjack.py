############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Set up the game
import day11_art
import random
lst_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Show welcome information
print(day11_art.logo)

# Function to draw a requested number of cards
def draw_cards(int_num_cards_dc):
    """Draw the specified number of cards, return list of cards

    Args:
        int_num_cards_dc (int): Number of cards to draw

    Returns:
        list[int]: List of cards
    """
    lst_hand_cards_dc = []
    for _ in range(0, int_num_cards_dc):
        int_new_card = random.choice(lst_cards)
        lst_hand_cards_dc.append(int_new_card)
    return lst_hand_cards_dc

# Function to calculate current score
def calculate_score(lst_hand_cards_cs):
    """Adds up all the cards in the list, returns the score

    Args:
        lst_cards (list): A list of cards (ints)

    Returns:
        int: The sum of all the cards in the list
    """
    return sum(lst_hand_cards_cs)

def determine_winner():
    print(f"Computer had {int_dealer_score} and you had {int_player_score}.")
    if int_dealer_score > 21:
        print("Computer busted. You win!")
    elif int_dealer_score > int_player_score:
        print("You lose. Sad.")
    elif int_dealer_score == int_player_score:
        print("Draw. Nobody wins. Boring.")
    else:
        print("You win!")

# Begin main loop for playing the game
boo_game_continue = True
while boo_game_continue:
    # Reset hands to empty
    lst_dealer_hand = []
    lst_player_hand = []
    # Draw initial hands
    lst_dealer_hand.extend(draw_cards(2))
    int_dealer_score = calculate_score(lst_dealer_hand)
    lst_player_hand.extend(draw_cards(2))
    int_player_score = calculate_score(lst_player_hand)

    # Set up while loop variables
    boo_draw_continue = True
    boo_busted = False

    # Check for Blackjacks
    if int_dealer_score == 21 and int_player_score == 21:
        print("Double Blackjack!! Draw.")
        boo_draw_continue = False
    elif int_dealer_score == 21:
        print("Blackjack!! Computer wins. Sad.")
        boo_draw_continue = False
    elif int_player_score == 21:
        print("Blackjack!! You win.")
        boo_draw_continue = False

    # Begin loop for drawing new cards

    while boo_draw_continue:    
        # Print status
        int_player_score = calculate_score(lst_player_hand)
        print(f"Your cards: {lst_player_hand}, current score: {int_player_score}") 
        print(f"Computer's first card: {lst_dealer_hand[0]}")

        # Ask if user wants another card
        chr_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if chr_another_card == 'n':
            boo_draw_continue = False
        else:
            lst_player_hand.extend(draw_cards(1))

        # Check for bust
        int_player_score = calculate_score(lst_player_hand)
        # Handle the case of an Ace
        if int_player_score > 21 and 11 in lst_player_hand:
            print("You went over 21, but you had at least one Ace. We've turned all Aces into ones.")
            for i, n in enumerate(lst_player_hand):
                if n == 11:
                    lst_player_hand[i] = 1
        if int_player_score > 21:
            print(f"You busted with {int_player_score} points! Computer wins. :-(")
            boo_draw_continue = False
            boo_busted = True

    # Add cards to dealer hand
    int_dealer_score = 0
    while int_dealer_score < 17:
        lst_dealer_hand.extend(draw_cards(1))
        int_dealer_score = calculate_score(lst_dealer_hand)

    # If player did not bust, determine winner
    if boo_busted == False:
        determine_winner()

    # Check if user wants to play another game
    chr_continue = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    if chr_continue == 'y':
        boo_game_continue = True
    else:
        boo_game_continue = False
