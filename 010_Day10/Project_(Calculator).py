from art import logo
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# ******************************************
print(logo)
# Add


def add(n1, n2):
    return n1+n2

# subtract


def subtract(n1, n2):
    return n1-n2

# multiply


def multiply(n1, n2):
    return n1*n2

# divide


def divide(n1, n2):
    return n1/n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What's the First number? "))
    for symbol in operation:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation")
        num2 = float(input("What's the next number? "))
        calculation_funtion = operation[operation_symbol]
        answer = calculation_funtion(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}:") == "y":
            num1 = answer
        else:
            should_continue = False
            cls()
            calculator()


calculator()


# NOTES mistakes
# # if ask == "+":
# #     answer = add(num1,num2)
# # elif ask == "-":
# #     answer = subtract(num1,num2)
# # elif ask == "*":
# #     answer = multiply(num1,num2)
# # elif ask == "/":
# #     answer = divide(num1,num2)

# calculation_funtion = operation[ask]
# answer = calculation_funtion(num1,num2)
