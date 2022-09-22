from data import MENU, resources

is_ready = True
profit = 0


def is_resource_sufficient(order_ind):
    for item in order_ind:
        if order_ind[item] >= resources[item]:
            print(f"Sorry  there is not enough {item}")
            return False
        return True


def process_coin():
    print("Please insert coins.")
    quaters = float(input("how many quarters?:"))
    dimes = float(input("how many dimes?:"))
    nickles = float(input("how many nickles?:"))
    pennies = float(input("how many pennies?:"))
    total_money = (0.25*quaters) + (0.10*dimes) + \
        (0.05*nickles) + (0.01 * pennies)
    print(total_money)
    return total_money


def transaction_succesful(money_recived, drink_cost):
    if money_recived >= drink_cost:
        reamaing_money = round(money_recived-drink_cost, 2)
        print(f"Here is ${reamaing_money} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while is_ready:
    coffe = input("What would you like? (espresso/latte/cappuccino):")

    if coffe == "off":
        is_ready = False
    elif coffe == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milf: {resources['milk']}ml")
        print(f"Coffe: {resources['coffee']}ml")
        print(f"Money: {resources['water']}ml")
    else:
        drink = MENU[coffe]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if transaction_succesful(payment, drink["cost"]):
                make_coffee(coffe, drink["ingredients"])
