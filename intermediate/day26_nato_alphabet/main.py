# List comprehension
numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Angela"
letters_list = [letter for letter in name if letter != "n"]
print(letters_list)

doubled = [n * 2 for n in range(1, 5)]
print(doubled)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)