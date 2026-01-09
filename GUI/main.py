from tkinter import *

def button_clicked():
    my_label.config(text=f"{input.get()}")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100,pady=200)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text",padx=50,pady=50)
my_label.grid(column=0,row=0)

#Button
button = Button(text="Click me", command=button_clicked)
button.config(padx=50,pady=50)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
input.grid(column=3,row=2)


window.mainloop() 