from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pasword_genarator():
    password_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    password = []

    password_letters = [choice(letters) for i in range(randint(8,10))]
    password_symbols = [choice(symbols) for i in range(randint(2,4))] 
    password_numbers = [choice(numbers) for i in range(randint(2,4))] 

    password = password_letters+password_numbers+password_symbols
    shuffle(password)
    
    pass_letters = "".join(password)

    password_input.insert(0,f"{pass_letters}")

    pyperclip.copy(f"{pass_letters}")
    pyperclip.paste()

# ---------------------------- SAVE PASSWORD ------------------------------- #
new_data = {}

def save():
    global new_data
    web_name = website_input.get()
    gmail = email_input.get()
    password_name = password_input.get()
    new_data = {web_name: {
        "email": gmail,
        "password": password_name
    }}

    if len(web_name) == 0 or len(password_name) == 0:
        messagebox.showwarning(title="Ooops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)

def search_password():
    web_page = website_input.get().title()
    try:
        with open("data.json") as data_file:
            password_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found")
    else:
        if web_page in password_data:
            gmail = password_data[web_page]["email"]
            pass_code = password_data[web_page]["password"]
            messagebox.showinfo(title="Passwor Info", message=f"Gmail: {gmail}\nPassword: {pass_code}")
        else:
            messagebox.showinfo(title="Passwor Info", message=f"No details on {web_page} exists")
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50,pady=50)
window.title("Password Generator")

my_label = Label()

canvas = Canvas(width=200,height=200)
ImgPath = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=ImgPath)
canvas.grid(row=0, column=1)

website_name = Label(text="Website:")
website_name.grid(column=0,row=1)

website_input = Entry(width=21)
website_input.grid(column=1,row=1, sticky="EW")
website_input.focus()

search_button = Button(text="Search", command=search_password)
search_button.grid(row=1, column=2, sticky="EW")

email_name = Label(text="Email/Username:")
email_name.grid(column=0,row=2)

email_input = Entry(width=35)
email_input.grid(column=1,row=2,columnspan=2, sticky="EW")
email_input.insert(0, "pssg2103@gmail.com")

password = Label(text="Password:")
password.grid(column=0,row=3)

password_input = Entry(width=21)
password_input.grid(column=1,row=3, sticky="EW")

generate_password = Button(text="Generate Password", width=15, command=pasword_genarator)
generate_password.grid(column=2,row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1,row=4,columnspan=2, sticky="EW")

window.mainloop()