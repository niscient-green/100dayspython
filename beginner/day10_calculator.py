import day10_art


# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


# define acceptable operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# display logo
print(day10_art.logo)


# function to calculate all values, recursive
def calculator():
    boo_answer = False
    boo_continue = True

    # while user selects to continue, perform calculations
    while boo_continue:
        # ask user for first number only if there is no existing answer
        if boo_answer == False:
            num1 = float(input("What is the first number? "))
        else:
            num1 = answer

        # ask user for operator
        list_of_operators = ""
        for op in operations:
            list_of_operators += op + " "
        operator = input(f"Which operator ( {list_of_operators})? ")

        # ask user for second number
        num2 = float(input("What is the next number? "))

        # calculate result, print answer
        answer = operations[operator](num1, num2)
        boo_answer = True
        print(f"Answer: {num1} {operator} {num2} = {answer}")

        # ask user whether to continue
        chr_continue = input(
            f"Type 'y' to continue calculating with {answer}, type 'c' to start a new calculation, or type 'n' to exit: "
        )
        if chr_continue == "n":
            boo_continue = False
        elif chr_continue == "c":
            calculator()
            boo_continue = False


calculator()
