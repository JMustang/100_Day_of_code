import email
from lib2to3.pygram import pattern_symbols
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pas_letters = [choice(letters) for _ in range(randint(10, 15))]
    pas_symbols = [choice(symbols) for _ in range(randint(4, 8))]
    pas_numbers = [choice(numbers) for _ in range(randint(4, 8))]

    password_list = pas_letters + pas_numbers + pas_symbols
    shuffle(password_list)

    password = ''.join(password_list)
    entry_3.insert(0, password)
    pyperclip.copy(password)

    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()

    if website == '' or password == '':
        messagebox.showinfo("Error", "Please enter all fields")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f'These are the details entered: \nEmail: {email}\nPassword: {password} '
            f'Is it ok to save?'
        )

        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                entry_1.delete(0, END)
                entry_3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
wind = Tk()
wind.title('Password Manager')
wind.config(padx=50, pady=50, bg='black')


# Canvas
canvas = Canvas(width=200, height=200, bg='black', highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
label_1 = Label(text='Website:', bg='black', fg='white')
label_1.grid(row=1, column=0)
label_2 = Label(text='Email/Username:', bg='black', fg='white')
label_2.grid(row=2, column=0)
label_3 = Label(text='Password:', bg='black', fg='white')
label_3.grid(row=3, column=0)

# Entry
entry_1 = Entry(width=35)
entry_1.grid(row=1, column=1, columnspan=2)
entry_1.focus()
entry_2 = Entry(width=35)
entry_2.insert(0, 'eecfredes@gmail.com')
entry_2.grid(row=2, column=1, columnspan=2)
entry_3 = Entry(width=21)
entry_3.grid(row=3, column=1)

# Buttons
button_1 = Button(text='Generate Password', command=generate_password)
button_1.grid(row=3, column=2, columnspan=2)

button_2 = Button(text='ADD', width=35, bg='green', fg='white', command=save)
button_2.grid(row=4, column=1, columnspan=2)


wind.mainloop()
