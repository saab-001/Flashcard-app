from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = (pandas.read_csv("Data/words_to_learn.csv")).to_dict(orient="records")
except FileNotFoundError:
    data = (pandas.read_csv("Data/french_words.csv")).to_dict(orient="records")

current_card = {}


def data_modifier():
    global current_card, data
    data.remove(current_card)
    new_data = pandas.DataFrame(data)
    pandas.DataFrame.to_csv(new_data, "Data/words_to_learn.csv", index=False)
    word_generator()


def word_generator():
    global current_card, timer

    window.after_cancel(timer)

    current_card = random.choice(data)
    fr_word = current_card["French"]
    screen.itemconfig(card, image=flash_card_fr)
    screen.itemconfig(lang, text="French", fill="black")
    screen.itemconfig(word, text=fr_word, fill="black")

    timer = timer = window.after(3000, change_card)


def change_card():
    en_word = current_card["English"]

    screen.itemconfig(card, image=flash_card_en)
    screen.itemconfig(lang, text="English", fill="white")
    screen.itemconfig(word, text=en_word, fill="white")


window = Tk()
window.title("Flash It")
window.config(width=800, height=600, bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(3000, change_card)

# Images
flash_card_fr = PhotoImage(file="images/card_front.png")
flash_card_en = PhotoImage(file="images/card_back.png")
right_icon = PhotoImage(file="images/right.png")
wrong_icon = PhotoImage(file="images/wrong.png")

# Flash card
screen = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
card = screen.create_image(400, 265, image=flash_card_fr)

# Text on Flash card

lang = screen.create_text(400, 130, text="Text", font=("Arial", 40, "italic"), justify="center")
word = screen.create_text(400, 265, text="word", font=("Arial", 60, "bold"), justify="center")

screen.grid(row=0, column=0, columnspan=2)

# Buttons
known_button = Button(image=right_icon, border=0, highlightthickness=0, command=data_modifier)
known_button.grid(row=1, column=0)

unknown_button = Button(image=wrong_icon, border=0, highlightthickness=0, command=word_generator)
unknown_button.grid(row=1, column=1)

word_generator()
window.mainloop()
