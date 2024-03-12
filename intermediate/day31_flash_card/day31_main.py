# Flash card program to learn multiple languages
# Import packages ---------------------------------------------------------------------------------
from tkinter import *
import pandas as pd
import random

# Set constants, globals---------------------------------------------------------------------------
BG_COLOR = "#B1DDC6"
CARD_COLOR = "white"
WINDOW_PADDING = 50
FONT_LANG = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
lang_from_str = ""
lang_to_str = ""
LANG_FROM_COLOR = "black"
LANG_TO_COLOR = "white"
words_to_learn_dct = {}
current_word_lst = []
flip_timer = None


# Handle words dictionary -------------------------------------------------------------------------
def import_words():
    # Import and build the dataframe for the words list
    global lang_from_str, lang_to_str, words_to_learn_dct

    # Try to open the remaining words to learn. If not found, use default csv.
    try:
        words_df = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        words_df = pd.read_csv("data/french_words.csv")

    lang_from_str = list(words_df.columns)[0]
    lang_to_str = list(words_df.columns)[1]

    # Convert to dict
    words_to_learn_dct = {row[lang_from_str]: row[lang_to_str] for (index, row) in words_df.iterrows()}


def write_unknown():
    # Write remaining unknown words to file
    global words_to_learn_dct
    words_to_learn_df = pd.DataFrame.from_dict(words_to_learn_dct, orient="index")
    words_to_learn_df.index.names = [lang_from_str]
    words_to_learn_df.rename(columns={0: lang_to_str}, inplace=True)
    words_to_learn_df.to_csv("data/words_to_learn.csv")


# Update card -------------------------------------------------------------------------------------
# Pick a word, update card
def pick_word():
    global flip_timer, current_word_lst

    # Make sure the canvas has the front image
    canvas.itemconfig(canvas_img, image=card_front_img)

    # Get a new word from the dictionary
    global words_to_learn_dct, current_word_lst
    current_word_str = random.sample(list(words_to_learn_dct), 1)[0]
    current_word_lst = [current_word_str, words_to_learn_dct[current_word_str]]
    canvas.itemconfig(lang_lbl, text=lang_from_str, fill=LANG_FROM_COLOR)
    canvas.itemconfig(word_lbl, text=current_word_lst[0], fill=LANG_FROM_COLOR)

    # Wait for user to guess
    flip_timer = window.after(3000, flip_card)


def flip_card():
    # Show the lang_to side of the card
    global current_word_lst
    canvas.itemconfig(lang_lbl, text=lang_to_str, fill=LANG_TO_COLOR)
    canvas.itemconfig(word_lbl, text=current_word_lst[1], fill=LANG_TO_COLOR)
    canvas.itemconfig(canvas_img, image=card_back_img)


def known_word():
    # If user knows word, remove from dictionary
    global flip_timer, words_to_learn_dct
    # Cancel any existing flip timers
    window.after_cancel(flip_timer)
    del words_to_learn_dct[current_word_lst[0]]
    write_unknown()
    pick_word()


def unknown_word():
    # If the user doesn't know word, keep in dictionary for future study
    global flip_timer
    # Cancel any existing flip timers
    window.after_cancel(flip_timer)
    pick_word()


# Create UI ---------------------------------------------------------------------------------------
# Create window
window = Tk()
window.title("Niscient's Flashy")
window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=BG_COLOR)

# Create canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BG_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(410, 250, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

# Create buttons
wrong_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=wrong_img, highlightthickness=0, command=unknown_word)
unknown_btn.grid(row=1, column=0)
right_img = PhotoImage(file="images/right.png")
known_btn = Button(image=right_img, highlightthickness=0, command=known_word)
known_btn.grid(row=1, column=1)


# Create labels
lang_lbl = canvas.create_text(400, 150, text="", font=FONT_LANG)
word_lbl = canvas.create_text(400, 263, text="", font=FONT_WORD)


# Main program loop -------------------------------------------------------------------------------
import_words()
pick_word()
window.mainloop()
