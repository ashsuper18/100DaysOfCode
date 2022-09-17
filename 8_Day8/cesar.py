from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True


def ceaser(plain_text, shift_amount, direction):
    cipher_text = ""
    for char in plain_text:
        # to keep the integer as it is in the message
        if char in alphabet:
            position = alphabet.index(char)
            if direction == "encode":
                new_position = position + shift_amount
            elif direction == "decode":
                new_position = position - shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"The {direction}d text is {cipher_text}")


while should_continue:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
        print("Wrong Input ❌")
        exit()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    ceaser(plain_text=text, shift_amount=shift, direction=direction)
    result = input("Do you want to continue? Type 'Yes' or 'No': ").lower()
    if result == "no":
        should_continue = False
        print("GoodBye👋")


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")


# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The encoded text is {plain_text}")


# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("Wrong Input")
