from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    choice = input(f'What would you like? ({menu.get_items()}): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(choice)
        if order:  # not needed for code to work, keeps program from crashing if input doesn't match any options
            if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
