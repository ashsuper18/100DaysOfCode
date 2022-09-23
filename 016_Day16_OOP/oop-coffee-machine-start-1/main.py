from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating an object from class (Blueprint)
mymoney_machine = MoneyMachine()
mycoffee_maker = CoffeeMaker()
# mymenu_item = MenuItem()
my_menu = Menu()

is_on = True


while is_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        mymoney_machine.report()
        mycoffee_maker.report()
    else:
        drink = my_menu.find_drink(choice)
        if mycoffee_maker.is_resource_sufficient(drink):
            if mymoney_machine.make_payment(drink.cost):
                mycoffee_maker.make_coffee(drink)

            # name = mymenu_item.name()
            # cost = mymenu_item.cost(name)
