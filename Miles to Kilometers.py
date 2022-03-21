from tkinter import *

# Sets window configuration
window = Tk()
window.title("Measurement Converter")
window.minsize(width=200, height=150)
window.config(padx=15, pady=40)


# Called later to convert provided miles to km on a button press
def conversion():
    miles = float(mileBox.get())
    km = (miles * 9 / 5) + 32
    kmReturn.config(text=str(km))


# Sets up input box for miles and the label identifying it
mileBox = Entry(width=5)
mileBox.grid(column=1, row=0)
mileLabel = Label(text="Miles")
mileLabel.grid(column=2, row=0)

# Writes the equal label
equalTo = Label(text="is equal to")
equalTo.grid(column=0, row=1)

# Sets the returned conversion of Km and identifies it
kmReturn = Label(text="0")
kmReturn.grid(column=1, row=1)
kmLabel = Label(text="Km")
kmLabel.grid(column=2, row=1)

# The Button
convertButton = Button(text="Convert", command=conversion)
convertButton.grid(column=1, row=2)

# Tells the window to stay open
window.mainloop()