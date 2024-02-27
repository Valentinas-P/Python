from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

IS_GAME_OVER = False

available_drinks = Menu()
mr_coffee = CoffeeMaker()
mr_pay = MoneyMachine()

while not IS_GAME_OVER:
    user_requirements = input(f"What would you like? ({available_drinks.get_items()}): ").lower()
    chosen_drink = available_drinks.find_drink(user_requirements)
    if user_requirements == "report":
        mr_coffee.report()
        mr_pay.report()
    elif mr_coffee.is_resource_sufficient(chosen_drink):
        if mr_pay.make_payment(chosen_drink.cost):
            mr_coffee.make_coffee(chosen_drink)
            mr_coffee.report()
            mr_pay.report()
