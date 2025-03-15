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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def print_machine():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction(money_received, drink_cost):
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
    for item in order:
        resources[item] -= order[item]
    print(f"Here is your {drink_name} ️. Enjoy!")

on = True
while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print(f"Profit: ${profit}")
        on = False
    elif choice == "report":
        print_machine()
    elif choice in MENU:
        if resource_sufficient(MENU[choice]["ingredients"]):
            if transaction(process_coins(), MENU[choice]["cost"]):
                make_coffee(choice, MENU[choice]["ingredients"])
    else:
        print("Invalid choice!")