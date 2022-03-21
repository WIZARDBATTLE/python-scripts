import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Oswald", 6, "normal")

screen = turtle.Screen()
screen.title("State Name Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = (screen.textinput(title=f"Guess the State | {len(guessed_states)}/50", prompt="Which state would you like"
                                                                                           " to guess?")).title()
    if answer == "exit".title():
        break
    if answer in states:
        guessed_states.append(answer)
        write = turtle.Turtle()
        write.hideturtle()
        write.penup()
        location = data[data.state == answer]
        write.goto(int(location.x), int(location.y))
        write.write(answer)


screen.exitonclick()