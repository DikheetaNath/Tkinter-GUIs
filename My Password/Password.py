from tkinter import *
from tkinter import messagebox
import json
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from RandomPasswordGenerator import Randompassword


def generate_random_password():
    new_password = Randompassword()
    password_input.insert(0, string=new_password.password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_ = website_input.get()
    mail_in = mail_input.get()
    passw = password_input.get()
    new_data = {
        website_: {
            "email": mail_in,
            "password": passw
        }
    }

    if len(website_) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Warning!", message="Do not leave fields empty")

    else:
        if not os.path.exists("Passwords.json") or os.stat("Passwords.json").st_size == 0:
            with open("Passwords.json", "w") as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            try:
                with open("Passwords.json", "r") as password_file:
                    data = json.load(password_file)
            except json.JSONDecodeError:
                data = {}
            data.update(new_data)
            with open("Passwords.json", "w") as password_file:
                json.dump(data, password_file, indent=4)
        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
locker = PhotoImage(file=r"C:\Users\dikhe\Downloads\Tkinter GUI\My Password\logo.png")
canvas.create_image(100, 100, image=locker)
canvas.grid(row=0, column=1)

# Labels:
website = Label(text="Website:")
website.grid(row=1, column=0)

mail = Label(text="Email/Username:")
mail.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

# text input:

website_input = Entry(width=45)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

mail_input = Entry(width=45)
mail_input.grid(row=2, column=1, columnspan=2)
mail_input.insert(0, string="@gmail.com")

password_input = Entry(width=25)
password_input.grid(row=3, column=1)

# Buttons:
Add = Button(text="Add", width=36, command=save)
Add.grid(row=4, column=1, columnspan=2)

generate = Button(text="Generate Password", width=20, command=generate_random_password)
generate.grid(row=3, column=2)

search = Button(text="Search")

window.mainloop()
