from tkinter import *
import pandas
from random import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orignal_data = pandas.read_csv("data/french_words.csv")
    to_learn = orignal_data.to_dict(orient="records")
else:
    to_learn = words_data.to_dict(orient="records")

window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_tick = PhotoImage(file="images/right.png")
wrong_tick = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.create_image(400,263, image=card_front)
    canvas.create_text(400,150, text="French", font=("Arial", 40, "italic"), fill="black")
    canvas.create_text(400,263, text=f"{current_card["French"]}", font=("Arial", 60, "bold"), fill="black")
    canvas.grid(row=0,column=0, columnspan=2)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.create_image(400,263, image=card_back)
    canvas.create_text(400,150, text="English", font=("Arial", 40, "italic"), fill="white")
    canvas.create_text(400,263, text=f"{current_card["English"]}", font=("Arial", 60, "bold"), fill="white")
    canvas.grid(row=0,column=0, columnspan=2)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))

    need_to_learn = pandas.DataFrame(to_learn)
    need_to_learn.to_csv("data/words_to_learn.csv", index=False)

    next_card()

flip_timer = window.after(3000, func=flip_card)
next_card()

right_button = Button(image=right_tick, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=0)

wrong_button = Button(image=wrong_tick, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1,column=1)

window.mainloop()

