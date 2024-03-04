################### Scope ####################
enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")