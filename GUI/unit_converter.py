from tkinter import *
import math

window = Tk()
window.minsize(width=250, height=100)
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

def unit_converter():
    ans = round(int(user_input.get()) * 1.609, 2)
    answer_label.config(text=f"{ans}")

user_input = Entry(width=5)
user_input.grid(column=1,row=0)

miles_unit = Label(text="Miles")
miles_unit.grid(column=2,row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)

answer_label = Label(text="0")
answer_label.grid(column=1,row=1)

km_unit = Label(text="Km")
km_unit.grid(column=2,row=1)

calculate_button = Button(text="Calculate",command=unit_converter)
calculate_button.grid(column=1,row=2)





window.mainloop()
