# Password Generator Project
from hashlib import new
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# NOTES Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pwd_list = []
for char in range(1, nr_letters+1):
    random_char = random.choice(letters)
    pwd_list.append(random_char)
    # print(pwd)
for sym in range(1, nr_symbols+1):
    pwd_list += random.choice(symbols)
for number in range(1, nr_numbers+1):
    random_sym = random.choice(numbers)
    pwd_list += random_sym
random.shuffle(pwd_list)
# print(pwd_list)

stringpwd = ""
for char in pwd_list:
    stringpwd += char
print(f"Your Generated Password is {stringpwd}")

# NOTES Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# pwd = ""
# for char in range(1,nr_letters+1):
#     random_char=random.choice(letters)
#     pwd = pwd + random_char
#     # print(pwd)
# for sym in range(1,nr_symbols+1):
#     pwd += random.choice(symbols)
# for number in range(1,nr_numbers+1):
#     random_sym = random.choice(numbers)
#     pwd += random_sym
# print(pwd)
