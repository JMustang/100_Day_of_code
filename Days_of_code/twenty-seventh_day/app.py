from tkinter import *
from turtle import position

window = Tk()

window.title("GUI python app")
window.minsize(width=500, height=300)

# Label
label = Label(text="Hello World", font=(
    "Arial", 20, "bold"))
label.config(text="new Hello World")
label.place(x=150, y=100)
# label.pack()


def button_clicked():
    new_text = input.get()
    label.config(text=new_text)


# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry()
input.pack()
# input.get()


window.mainloop()
