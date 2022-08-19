from tkinter import *
import pandas
import random
from canvas import MainWindow
BACKGROUND_COLOR = "#B1DDC6"
# -----------------------------DATA-------------------------------#

data = pandas.read_csv("data/english_words.csv")
polish_list = data["Polish"].to_list()
english_list = data["English"].to_list()

number = random.randint(0, len(polish_list))
random_polish_word = polish_list[number]
random_english_word = english_list[number]

# -----------------------------UI-------------------------------- #

window = Tk()
window.config(width=900, height=900, background=BACKGROUND_COLOR)
window.title("FlashCard")

MainWindow(window)

window.mainloop()




