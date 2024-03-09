from menu import Menu, MenuItem  # Importing necessary classes
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating instances of the required classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True  # Setting the initial state of the coffee machine to on

# Main loop to keep the coffee machine running
while is_on:
    options = menu.get_items()  # Get available drink options from the menu
    choice = input(f"What would you like? ({options})")  # Ask the user for their choice

    if choice == "off":  # If user wants to turn off the machine
        is_on = False  # Set the state to off, exiting the loop
    elif choice == "report":  # If user wants to generate a report
        coffee_maker.report()  # Print the report of resources
        money_machine.report()  # Print the report of profits
    else:
        drink = menu.find_drink(choice)  # Find the selected drink from the menu

        # Check if the selected drink is available, machine has enough resources, and payment is successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)  # Make the selected drink


