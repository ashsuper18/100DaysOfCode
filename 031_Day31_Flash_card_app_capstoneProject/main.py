from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# *****************getting data from file*****************#
try:
    data = pd.read_csv(
        r"031_Day31_Flash_card_app_capstoneProject\data\words_to_learn.csv")
except FileNotFoundError:
    orginal_data = pd.read_csv(
        r"031_Day31_Flash_card_app_capstoneProject\data\french_words.csv")
    to_learn = orginal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background, image=bg_imagef)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=bg_imagee)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(
        r"031_Day31_Flash_card_app_capstoneProject\data\words_to_learn.csv", index=False)
    next_card()


# *****************UI Setup********************************
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
bg_imagef = PhotoImage(
    file=r"031_Day31_Flash_card_app_capstoneProject\images\card_front.png")
bg_imagee = PhotoImage(
    file=r"031_Day31_Flash_card_app_capstoneProject\images\card_back.png")

card_background = canvas.create_image(400, 263, image=bg_imagef)
card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

image1 = PhotoImage(
    file=r"031_Day31_Flash_card_app_capstoneProject\images\wrong.png")
image2 = PhotoImage(
    file=r"031_Day31_Flash_card_app_capstoneProject\images\right.png")

button_wrong = Button(image=image1, highlightthickness=0,
                      relief="flat", bg=BACKGROUND_COLOR, command=next_card)
button_wrong.grid(row=1, column=0)
button_right = Button(image=image2, highlightthickness=0,
                      relief="flat", bg=BACKGROUND_COLOR, command=is_known)
button_right.grid(row=1, column=1)

next_card()


window.mainloop()
