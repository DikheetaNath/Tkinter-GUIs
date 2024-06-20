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
    website_entry = website_input.get()
    mail_entry = mail_input.get()
    password_entry = password_input.get()
    new_data = {
        website_entry: {
            "email": mail_entry,
            "password": password_entry
        }
    }

    if len(website_entry) == 0 or len(password_entry) == 0:
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


# ---------------------------- SEARCH PASSWORD  ------------------------------- #

def find_password():
    website_name_dict = website_input.get()
    if not os.path.exists("Passwords.json") or os.stat("Passwords.json").st_size == 0:
        messagebox.showinfo(title="ERROR", message="No data file found")
    else:
        try:
            with open("Passwords.json", "r") as file:
                data = json.load(file)
                print(data[website_name_dict])
        except KeyError:
            messagebox.showinfo(title="ERROR", message="No such Website found")
        else:
            email_dict = "email"
            password_dict = "password"
            messagebox.showinfo(title=f"{website_name_dict}", message=f"Your mail is for this website "
                                                                      f"is {data[website_name_dict][email_dict]} \n "
                                f"and password is {data[website_name_dict][password_dict]} ")

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

website_input = Entry(width=25)
website_input.grid(row=1, column=1)
website_input.focus()

mail_input = Entry(width=40)
mail_input.grid(row=2, column=0, columnspan=3)
mail_input.insert(0, string="@gmail.com")

password_input = Entry(width=25)
password_input.grid(row=3, column=1)

# Buttons:
Add = Button(text="Add", width=36, command=save)
Add.grid(row=4, column=1, columnspan=2)

generate = Button(text="Generate Password", width=20, command=generate_random_password)
generate.grid(row=3, column=2)

search = Button(text="Search", width=20, fg="blue", command=find_password)
search.grid(row=1, column=2)

window.mainloop()
