from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

can_continue = True
resources_list = CoffeeMaker()
menu_items = Menu()
money_machine = MoneyMachine()

while can_continue:
    user_input = input(f"What would you like? ({menu_items.get_items()})").lower()
    if user_input == "report":
        resources_list.report()
        money_machine.report()
    elif user_input == "off":
        can_continue = False
    else:
        user_choice = menu_items.find_drink(user_input)
        if resources_list.is_resource_sufficient(user_choice) and money_machine.make_payment(user_choice.cost):
            resources_list.make_coffee(user_choice)