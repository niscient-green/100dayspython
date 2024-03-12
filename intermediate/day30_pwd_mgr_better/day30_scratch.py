# File not found error
try:
    file = open("what_a_file.txt")
    a_dct = {"key" : "value"}
    print(a_dct["key"])
except FileNotFoundError:
    print("Error: file not found")
    file = open("what_a_file.txt", "w")
except KeyError as error_msg:
    print(f"Error: key not found. {error_msg}")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")


# Raise own exception

height = float(input("Height: "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters.")