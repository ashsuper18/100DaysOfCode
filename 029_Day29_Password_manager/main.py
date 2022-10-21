from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    # insted of using += we can use = and letter we can create pasword list and add all three lists
    random.shuffle(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    pswd_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = web_input.get()
    email = email_input.get()
    password = pswd_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"Entered Details:\n Email: {email}\n Passowrd:{password}\n Is it Correct?")
        if is_ok:
            with open("029_Day29_Password_manager\data.txt", "a") as data_file:
                data_file.write(f"{website} || {email} || {password}\n")
                web_input.delete(0, END)
                pswd_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="029_Day29_Password_manager\logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pswd_label = Label(text="Password:")
pswd_label.grid(row=3, column=0)


# Entries
web_input = Entry(width=52)
web_input.grid(row=1, column=1, columnspan=2, sticky="w")
web_input.focus()
email_input = Entry(width=52)
email_input.grid(row=2, column=1, columnspan=2, sticky="w")
email_input.insert(0, "ashsuper18@gmail.com")
pswd_input = Entry(width=33)
pswd_input.grid(row=3, column=1,  sticky="w")


# buttons
password_btn = Button(text="Generate Password", command=generate_password)
password_btn.grid(row=3, column=2)
# NOTES do not run a funciton in command like save_data()
add_btn = Button(text="Add", width=44, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2, sticky="w")


root.mainloop()
