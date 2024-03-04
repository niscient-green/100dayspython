import day8_art

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
int_length_alphabet = len(alphabet)

print(day8_art.logo)

# this is the main cipher function
def caesar_cipher(text, shift, direction):
    str_shifted_message = ""

    shift %= 26
    if direction == "decode":
        shift *= -1

    for char in text:
        try:
            int_alphabet_position = alphabet.index(char)
            int_shifted_position = int_alphabet_position + shift
            if int_shifted_position < 0:
                int_shifted_position += int_length_alphabet
            elif int_shifted_position >= int_length_alphabet:
                int_shifted_position -= int_length_alphabet
            str_shifted_letter = alphabet[int_shifted_position]
            str_shifted_message += str_shifted_letter
        except ValueError:
            str_shifted_message += char

    print(f"The {direction}d text is {''.join(str_shifted_message)}")


boo_continue = True
while boo_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(text, shift, direction)
    str_continue = input(
        "Would you like to continue the cipher program ('yes' or 'no')? "
    )
    if str_continue == "no":
        boo_continue = False