from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash It")
window.config(width=800, height=600, bg=BACKGROUND_COLOR, padx=50, pady=50)

flash_card_fr = PhotoImage(file="images/card_front.png")
flash_card_en = PhotoImage(file="images/card_back.png")

screen = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
screen.create_image(400, 265, image=flash_card_fr)
fr_word = "Bonjour"
screen.create_text(400, 130, text="French", font=("Arial", 40, "italic"), justify="center")
screen.create_text(400, 265, text=fr_word, font=("Arial", 60, "bold"), justify="center")
screen.grid(row=0, column=0, columnspan=2)

right_icon = PhotoImage(file="images/right.png")
wrong_icon = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_icon, border=0, highlightthickness=0)
right_button.grid(row=1, column=0)

wrong_button = Button(image=wrong_icon, border=0, highlightthickness=0)
wrong_button.grid(row=1, column=1)

window.mainloop()
