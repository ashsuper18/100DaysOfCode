import os
from unicodedata import name
from art import *
from game_data import data
import random
print(logo)

game_on = True
score = 0


def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


account_b = random.choice(data)


while game_on:
    # get random data from game_data file
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    # check follower
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    user_ans = input("Who has more followers? Type 'A' or 'B': ").lower()
    os.system('cls')
    print(logo)

    if check_answer(user_ans, a_follower, b_follower):
        # os.system('cls')
        score += 1
        # print(logo)
        print(f"You're right! Current Score:{score}")
    else:
        # os.system('cls')
        # print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_on = False
