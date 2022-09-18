
import random
import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
from art import logo

game_over = False

# Hint 4 *******************************************
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new=random.randint(0,len(cards)-1)
    return cards[new]
    # print(random_card)

# Hint 6,7,8*******************************************
def claculate_score(cards):
    # user_total = cards[0] + cards[1]
    # NOTES both above and below are doing same job
    user_total = sum(cards)
    if user_total == 21:
        return 0
    if 11 in cards and user_total > 21:
        cards.remove(11)
        cards.append(1)
    return user_total


def compare(user_score , computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose , oppent has Blackjack 😨"
    elif user_score ==0:
        return "Win with a Blackjack 😚"
    elif user_score>21:
        return "You went over. You Lose 😮"
    elif computer_score> 21:
        return "Computer went over. You Win!! 😂"
    elif user_score> computer_score:
        return "You Win!! 😂"
    else:
        return "You Lose 😪"

def play_game():
# Hint 5 *******************************************
    print(logo)

    user_card = []
    computer_card = []
    game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not game_over:
        user_score = claculate_score(user_card)
        computer_score = claculate_score(computer_card)

        print(f"User card: {user_card}, Your total is: {user_score}")
        print(f"computer card: {computer_card[0]}")
        # Hint 9 ************************************************
        if user_score==0 or computer_score ==0 or user_score>21:
            game_over= True
        else: 
            ask = input("Do you want to draw another card ✋? Type 'y' or 'n'.")
            if ask =="y":
                user_card.append(deal_card())
            else:
                game_over = True
            
    # Hint12 ****************************************************
    while computer_score != 0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score = claculate_score(computer_card)

        # print(compare(user_score , computer_score))
    print(compare(user_score, computer_score))
    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_card}, final score: {computer_score}")

while input("👉 Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    cls()
    play_game()
