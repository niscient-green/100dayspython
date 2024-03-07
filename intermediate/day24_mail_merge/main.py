# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Set globals
PLACEHOLDER = "[name]"

# Open the file of invites, create and return list of invites
def get_invites():
    with open("./Input/Names/invited_names.txt", mode="r") as invited_file:
        invited_names = invited_file.readlines()
        invited_file.close()
    return invited_names


# Open the starting letter, read and return the contents
def get_letter():
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
        letter_contents = letter_file.readlines()
        letter_file.close()
    return letter_contents


# Write out a letter for each invitee
letter_contents = get_letter()
for invitee in get_invites():
    # Update the letter content
    stripped_name = invitee.strip()
    new_letter = letter_contents
    new_letter[0] = new_letter[0].replace(PLACEHOLDER, stripped_name)
    output_file_name = f"./Output/ReadyToSend/letter_for_{stripped_name}.txt"
    with open(output_file_name, mode="w") as sending_file:
        sending_file.writelines(new_letter)
        sending_file.close()