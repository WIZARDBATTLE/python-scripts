from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#076937"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #

def resetTimer():
    window.after_cancel(TIMER)
    lifeLabel.config(text="This is your life")
    canvas.itemconfig(timer, text="00:00")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def startTimer():
    global REPS
    REPS += 1
    workTime = WORK_MIN * 60
    shortBreakTime = SHORT_BREAK_MIN * 60
    longBreakTime = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        countdown(longBreakTime)
        lifeLabel.config(text="BREAK BOI")
    elif REPS % 2 == 0:
        countdown(shortBreakTime)
        lifeLabel.config(text="BREAK BOI")
    else:
        countdown(workTime)
        lifeLabel.config(text="work time")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    countMin = math.floor(count / 60)
    countSec = count % 60
    if countSec < 10:
        countSec = f"0{countSec}"
    canvas.itemconfig(timer, text=f"{countMin}:{countSec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count - 1)
    else:
        startTimer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("This is so you don't go insane, little man")
window.config(padx=100, pady=100, bg=GREEN)

canvas = Canvas(width=200, height=223, bg=GREEN, highlightthickness=0)
tomatoPic = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomatoPic)
timer = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

lifeLabel = Label(text="This is your life", font=(FONT_NAME, 18, "bold"), bg=GREEN)
lifeLabel.grid(column=1, row=0)

startButton = Button(text="Start", command=startTimer)
startButton.grid(column=0, row=2)

resetButton = Button(text="Reset", command=resetTimer)
resetButton.grid(column=2, row=2)

window.mainloop()
