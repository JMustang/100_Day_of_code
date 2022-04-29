from tabnanny import check
from tkinter import *
from turtle import title
import math
# ---------------------------- CONSTANTS ------------------------------- #
GREEN = "#06FF00"
RED = "#e7305b"
ORANGE = "#FF7700"
DARK_PURPLE = "#251D3A"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f'00:00')
    title_label.config(text="Timer")
    check_mark.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 4 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=ORANGE)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = windows.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ''
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += '✓'
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Pymodoro")
windows.config(padx=100, pady=50, bg=DARK_PURPLE)


title_label = Label(text='Timer', fg=ORANGE,
                    bg=DARK_PURPLE, font=(FONT_NAME, 45))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=DARK_PURPLE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white',
                                font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


start_button = Button(text='Start', fg=RED,
                      bg='white', highlightthickness=1, command=start_timer)
start_button.grid(column=0, row=3)
reset_button = Button(text='Reset', fg=RED,
                      bg='white', highlightthickness=1, command=reset_timer)
reset_button.grid(column=2, row=3)

check_mark = Label(fg=GREEN, bg=DARK_PURPLE)
check_mark.grid(column=1, row=3)

windows.mainloop()
