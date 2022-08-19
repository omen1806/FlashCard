import pandas
import random

# -----------------------------DATA-------------------------------#

data = pandas.read_csv("data/english_words.csv")


class Data():

    def __init__(self):
        self.data_dict = data.to_dict(orient="records")
        self.english_random = self.data_dict[random.randint(0, len(self.data_dict)-1)]["English"]

    def front_word(self):
        return self.english_random

