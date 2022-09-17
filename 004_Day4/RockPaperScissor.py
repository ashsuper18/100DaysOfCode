import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

newlist = [rock, paper, scissors]

value1 = int(
    input("What do you choose? Type 0 = Rock, 1 = Paper or 2 = Scissor. :"))
my = newlist[value1]
print("Your move is " + str(my))


random_number = random.randint(0, 2)
selction = newlist[random_number]
print(f"Your oppent move is {selction}")

if value1 == 0 and random_number == 2:
    print("You win!!")
elif value1 >= 3 or random_number < 0:
    print("Invalid Number")
elif value1 == 1 and random_number == 0:
    print("You win!!")
elif value1 == 2 and random_number == 0:
    print("You Lose!")
elif value1 == 2 and random_number == 1:
    print("You Win!")
elif random_number > value1:
    print("You Lose")
elif value1 == random_number:
    print("Draw")
