import os
import day9_art

dct_bid = {}

print(day9_art.logo)

boo_continue = True
while boo_continue:
    str_bidder_name = input("What is your name? ")
    int_bid = int(input("What's your bid? $"))
    dct_bid[str_bidder_name] = int_bid

    str_more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if str_more_bidders == "no":
        boo_continue = False
    
    # clear the screen
    os.system('cls')

str_winner = max(dct_bid, key=dct_bid.get)
print(f"Winner is {str_winner} with a bid of ${dct_bid[str_winner]}.")