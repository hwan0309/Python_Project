from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
    options = menu.get_items()
    choice = input(f"무엇을 좋아하나요? ({options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingreadients =  coffee_maker.is_resource_sufficient(drink)
        is_payment_successful =  money_machine.make_payment(drink.cost)
        if is_enough_ingreadients and is_payment_successful:
            coffee_maker.make_coffee(drink)
