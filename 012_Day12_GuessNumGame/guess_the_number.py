import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("Number will be between 1 to 100")

level = input("Choose the difficulty. Type 'easy' or 'hard': ")

randomnumber = random.randint(1, 100)
# print(randomnumber)


def play():
    if level == "easy":
        attempt = 10
    elif level == "hard":
        attempt = 5

    while attempt != 0:
        print(f"You have {attempt} attempts remaining\n")
        Guess = int(input("Make a Guess: "))
        if Guess > randomnumber:
            print(f"Too High")
            attempt -= 1

        elif Guess < randomnumber:
            print(f"Too Low Try agin, Guess Again")
            attempt -= 1
        else:
            print("You Got it !!!!")
            return

        if attempt > 1:
            print("Guess Again")

    print(
        f"You've run out of guesses, you lose!\nThe number was {randomnumber}")


play()
