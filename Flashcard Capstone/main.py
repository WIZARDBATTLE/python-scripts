from tkinter import *
from pandas import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashcards Bitch!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
cardFront = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=cardFront)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=1, row=1)


window.mainloop()