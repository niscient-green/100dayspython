# Convert a string into a NATO alphabet word list

# Import packages
import pandas

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_word = input("Enter a word to convert: ").upper()
    try:
        code_words = [nato_alphabet_dict[letter] for letter in user_word]
    except KeyError:
        print("Please use alphabet characters only.")
        generate_phonetic()
    else:
        print(code_words)


generate_phonetic()
