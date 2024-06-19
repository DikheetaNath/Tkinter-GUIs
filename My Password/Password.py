from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from RandomPasswordGenerator import Randompassword


def generate_random_password():
    new_password = Randompassword()
    password_input.insert(0, string=new_password.password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = website_input.get()
    passw = password_input.get()

    if len(web) != 0 and len(passw) != 0:
        is_ok = messagebox.askokcancel(title="Are you sure?",
                                       message=f"Your website is {web} and your password is {passw}.Do you want to "
                                               f"save it?")
        if is_ok:
            with open("Passwords_text_file", mode="a") as password_file:
                password_file.write(
                    f"website:{web} | mail/username:{mail_input.get()} | password:{passw}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)

    else:
        messagebox.showinfo(title="Warning!", message="Do not leave fields empty")


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

window.mainloop()
