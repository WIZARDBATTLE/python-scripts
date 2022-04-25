from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Generates a random alphanumeric
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    [password_list.append(choice(letters)) for char in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for char in range(randint(2, 4))]
    [password_list.append(choice(numbers))for char in range(randint(2, 4))]
    shuffle(password_list)

    randomPassword = "".join(password_list)
    passwordInput.insert(0, randomPassword)
    pyperclip.copy(randomPassword)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# Saves login to passwords.txt
def saveLogin(website, username, password):
    print(f"{website}|{username}|{password}")
    loginDoc = open("passwords.txt", "a")
    loginDoc.write(f"{website}|{username}|{password}\n")
    loginDoc.close()

def pressAdd():
    website = websiteInput.get()
    username = userInput.get()
    password = passwordInput.get()
    loginData = {
        website: {
            "username/email": username,
            "password": password
        }
                }
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="You nincompoop", message="Fill out your dang fields doofus")
    else:
        try:
            with open("data.json", "r") as loginDoc:
                data = json.load(loginDoc)
        except FileNotFoundError:
            with open("data.json", "r") as loginDoc:
                json.dump(loginData, loginDoc, indent=4)
        else:
            data.update(loginData)
            with open("data.json", "w") as loginDoc:
                json.dump(loginData, loginDoc, indent=4)
        finally:
            loginDoc.close()
            websiteInput.delete(0, END)
            userInput.delete(0, END)
            passwordInput.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def findPassword():
    website = websiteInput.get()
    try:
        with open("data.json") as loginDoc:
            data = json.load(loginDoc)
    except FileNotFoundError:
        messagebox.showinfo(title= "Done goofed", message= "This doesn't exist. None of us do.")
    else:
        if website in data:
            email = data[website]["username/email"]
            password = data[website]["password"]
            messagebox.showinfo(title= "Here's your shit", message= f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title= "What do I look like, Google?", message= "There's nobody by that name here")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Keeper")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

websiteLabel = Label(text="Website:")
websiteLabel.grid(column=0, row=1)
userLabel = Label(text="Email/Username:")
userLabel.grid(column=0, row=2)
passwordLabel = Label(text="Password:")
passwordLabel.grid(column=0, row=3)

websiteInput = Entry(width=27)
websiteInput.grid(column=1, row=1)
websiteInput.focus()
userInput = Entry(width=43)
userInput.grid(column=1, row=2, columnspan=2)
passwordInput = Entry(width=27)
passwordInput.grid(column=1, row=3)

passwordButton = Button(text="Generate Password", command=generatePassword)
passwordButton.grid(column=2, row=3)

addButton = Button(width=43, text="Add", command=pressAdd)
addButton.grid(column=1, row=4, columnspan=2)

searchButton = Button(width=15, text="Search", command=findPassword)
searchButton.grid(column=2, row=1)

window.mainloop()