import sys
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
profit = 0
resources = {
    'water': 500,
    'milk': 250,
    'coffee': 76,
    'money': 0
}


def print_report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']
    print(f"The current resources are:\nWater: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def manage_resources(drink):
    for ingredient in MENU[drink]['ingredients']:
        current_amount = resources.get(ingredient)
        needed_amount = MENU[drink]['ingredients'].get(ingredient)
        if current_amount < needed_amount:
            print(f"Sorry there is not enough {ingredient}")
            break
        else:
            process_payment(drink)
            break


def process_payment(drink):
    total = int(input("How many Pennies? ")) * 0.01
    total += int(input("How many Nickles? ")) * 0.05
    total += int(input("How many Dimes? ")) * 0.1
    total += int(input("How many Quarters? ")) * 0.25
    drink_cost = MENU[drink]['cost']
    if total < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
    elif total == MENU[drink]['cost']:
        resources['money'] += total
        make_coffee(drink)
    else:
        refund = (total - drink_cost)
        resources['money'] += drink_cost
        print(f"Here is ${refund} in change")
        make_coffee(drink)


def make_coffee(drink):
    for ingredient in MENU[drink]['ingredients']:
        used_resource = MENU[drink]['ingredients'].get(ingredient)
        resources[ingredient] -= used_resource
    print(f"Here is your {drink}. Enjoy!")


def get_input():
    choice = input("What would you like? (espresso/latte/cappuccino) ")
    if choice == 'off':
        sys.exit()
    elif choice == 'report':
        print_report()
    else:
        manage_resources(choice)
    get_input()


if __name__ == '__main__':
    get_input()
