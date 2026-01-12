import pandas
import random

words_data = pandas.read_csv("data/french_words.csv")

french_word = random.choice(words_data["French"])
print(french_word)
eng_word = words_data[words_data.French == french_word].En
print(eng_word)

for (index,row) in words_data.iterrows():
    if row.French == words_data["French"][0]:
        print(row.English)
