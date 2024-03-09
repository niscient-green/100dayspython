# Convert a string into a NATO alphabet word list

# Import packages
import pandas

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word to convert: ").upper()
code_words = [nato_alphabet_dict[letter] for letter in user_word]
print(code_words)
