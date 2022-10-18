import pandas as pd
files = pd.read_csv(
    r"026_Day26_Listcomprehension\NATO-alphabet-start\nato_phonetic_alphabet.csv")
# print(files)

# TODO 1. Create a dictionary in this format:
new_dict = {value.letter: value.code for (key, value) in files.iterrows()}
# print(new_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a Word: ").upper()
output = [new_dict[letter] for letter in word]
print(output)

# print(new_dict['C'])
