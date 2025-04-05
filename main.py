"""
Coffee Machine Program

This program simulates a coffee machine that can make three types of drinks:
- Espresso: Strong coffee with no milk
- Latte: Coffee with steamed milk
- Cappuccino: Coffee with equal parts steamed milk and milk foam

The machine tracks resources (water, milk, coffee) and handles payments through coins.
Users can check resource levels and turn off the machine.
"""

# Menu dictionary containing drink recipes and costs
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Initial resources available in the machine
resources = {
    "water": 300,  # in milliliters
    "milk": 200,   # in milliliters
    "coffee": 100, # in grams
}
# Tracks the money earned by the machine
profit = 0  

def print_machine():
    """
    Prints the current resource levels and profit of the coffee machine.
    Shows water, milk, and coffee amounts, as well as total money earned.
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def resource_sufficient(order_ingredients):
    """
    Checks if there are enough ingredients to make the requested drink.
    
    Args:
        order_ingredients (dict): Dictionary containing required ingredients and their amounts
        
    Returns:
        bool: True if there are sufficient ingredients, False otherwise
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """
    Processes coin input from the user.
    Accepts quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢).
    
    Returns:
        float: Total amount of money inserted
    """
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction(money_received, drink_cost):
    """
    Processes the payment for a drink.
    
    Args:
        money_received (float): Amount of money inserted by the user
        drink_cost (float): Cost of the selected drink
        
    Returns:
        bool: True if payment is successful, False otherwise
    """
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order):
    """
    Makes the selected drink and updates the available resources.
    
    Args:
        drink_name (str): Name of the drink to make
        order (dict): Dictionary containing the ingredients needed
    """
    for item in order:
        resources[item] -= order[item]
    print(f"Here is your {drink_name} ️. Enjoy!")

# Main program loop
on = True
while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    # Handle special commands
    if choice == "off":
        print(f"Profit: ${profit}")
        on = False
    elif choice == "report":
        print_machine()
    # Process drink orders
    elif choice in MENU:
        if resource_sufficient(MENU[choice]["ingredients"]):
            if transaction(process_coins(), MENU[choice]["cost"]):
                make_coffee(choice, MENU[choice]["ingredients"])
    else:
        print("Invalid choice!")