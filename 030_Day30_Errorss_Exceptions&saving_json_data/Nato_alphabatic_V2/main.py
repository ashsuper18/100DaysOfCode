import pandas as pd
files = pd.read_csv("Nato_alphabatic\\nato_phonetic_alphabet.csv")
# print(files)
correct = True
new_dict  = {value.letter:value.code for (key,value) in files.iterrows()}
while correct:
    word = input("Enter a Word: ").upper()
    try:
        output = [new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letters in the alphabet please.")
    else:
        print(output)

        

# print(new_dict['C'])
 