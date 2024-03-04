from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create global variables
MENU = Menu()
COFFEEMAKER = CoffeeMaker()
MONEY = MoneyMachine()

boo_continue = True
while boo_continue:
    # Ask for input
    str_menu_choice = input(f"What would you like? ({MENU.get_items()}): ").lower()
    if str_menu_choice == "report":
        COFFEEMAKER.report()
        MONEY.report()
    elif str_menu_choice == "done":
        boo_continue = False
    else:
        obj_menu_choice = MENU.find_drink(str_menu_choice)
        if obj_menu_choice == "None":
            print("Could not find that drink.")
        else:
            if COFFEEMAKER.is_resource_sufficient(obj_menu_choice) and MONEY.make_payment(obj_menu_choice.cost):
                COFFEEMAKER.make_coffee(obj_menu_choice)