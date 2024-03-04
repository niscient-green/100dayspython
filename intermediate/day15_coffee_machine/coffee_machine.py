# Import data and packages
import data


# Function: Check if resources are sufficient for a drink
def check_resources(str_drink_choice):
    for resource in data.resources:
        if data.resources[resource] <= data.MENU[str_drink_choice]["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
        else:
            return True


# Function: print a report of the machine's resources
def resource_report():
    print(f"Water: {data.resources["water"]}ml")
    print(f"Milk: {data.resources["milk"]}ml")
    print(f"Coffee: {data.resources["coffee"]}g")
    print(f"Money: ${data.resources["money"]}")


# Function: Process coins
def process_coins(str_drink_choice):
    # Ask for coins
    print("Please insert coins.")
    int_quarters = int(input("how many quarters? "))
    int_dimes = int(input("how many dimes? "))
    int_nickels = int(input("how many nickels? "))
    int_pennies = int(input("how many pennies? "))

    # Sum total user paid and compare against drink cost
    flt_user_paid = int_quarters * 0.25 + int_dimes * 0.10 + int_nickels * 0.05 + int_pennies * 0.01
    flt_drink_cost = data.MENU[str_drink_choice]["cost"]
    if flt_user_paid >= flt_drink_cost:
        flt_change = flt_user_paid - flt_drink_cost
        print(f"Here is ${flt_change:.2f} in change.")
        data.resources["money"] += flt_drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


# Function: make the coffe chosen by the user
def make_coffee(str_drink_choice):
    # Remove the resources from the resources dictionary
    data.resources["water"] -= data.MENU[str_drink_choice]["ingredients"]["water"]
    data.resources["milk"] -= data.MENU[str_drink_choice]["ingredients"]["milk"]
    data.resources["coffee"] -= data.MENU[str_drink_choice]["ingredients"]["coffee"]
    print(f"Here is your {str_drink_choice}. Enjoy!")


# Function: handle a coffee order
def order_coffee():
    str_drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if str_drink_choice == "report":
        resource_report()
        return True
    elif str_drink_choice == "done":
        return False
    else:
        if check_resources(str_drink_choice) and process_coins(str_drink_choice):
            make_coffee(str_drink_choice)
        return True


# Main program loop
while order_coffee():
    pass

print("Thanks for using our coffee machine!")
