import os
import random
import hangman_art
import hangman_words

print(hangman_art.logo)
game_end = False
chosen_word = random.choice(hangman_words.word_list)
life = 6
# print(f'Pssst, the solution is {chosen_word}.')
wordLength = len(chosen_word)
lists = []

for number in range(wordLength):
    lists.append('_')
print(lists)
# while "_" in lists :
while not game_end:
    guess = input("Guess a letter: ").lower()
    def clear(): return os.system('cls')

    if guess in lists:
        print(f"You have already guessed {guess}")
    for position in range(wordLength):
        letter = chosen_word[position]
        if letter == guess:
            lists[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word you losse a life")
        life -= 1
        print(f"Reamining life is {life}")
        if life == 0:
            game_end = True
            print("You Lose")
            print(f'Pssst, the solution was {chosen_word}.')

    print(lists)

    if "_" not in lists:
        game_end = True
        print("you win")

    print(hangman_art.stages[life])
