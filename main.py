from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# -------------------- ------------------------------#

# -----------------------------DATA-------------------------------#

data = pandas.read_csv("data/english_words.csv")
polish_list = data["Polish"].to_list()
english_list = data["English"].to_list()

number = random.randint(0, len(polish_list))
random_polish_word = polish_list[number]
random_english_word = english_list[number]

# -----------------------------UI-------------------------------- #

def window():
    window = Tk()
    window.config(width=900, height=900, background=BACKGROUND_COLOR)
    window.title("FlashCard")

    canvas = Canvas(width=880, height=586, highlightthickness=0, background=BACKGROUND_COLOR)
    card_img = PhotoImage(file="images/card_front.png")
    canvas.create_image(440, 300,  image=card_img)
    upper_text_canvas = canvas.create_text(440, 200, text="Polski", fill=BACKGROUND_COLOR, font=("arial", 40, "italic"))
    lower_text_canvas = canvas.create_text(440, 330, text=random_polish_word, fill=BACKGROUND_COLOR, font=("arial", 50, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)

    right_button = Button()
    right_button_img = PhotoImage(file="images/right.png")
    right_button.config(image=right_button_img, pady=20)
    right_button.grid(column=0, row=1)

    wrong_button = Button()
    wrong_button_img = PhotoImage(file="images/wrong.png")
    wrong_button.config(image=wrong_button_img, pady=20)
    wrong_button.grid(column=1, row=1)

    window.mainloop()
window()