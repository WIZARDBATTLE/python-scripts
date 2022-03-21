import time
import turtle
from turtle import Screen
from Player import player
from Car_Manager import carManager
from Scoreboard import scoreboard

# Initializes screen and tells it to listen for key presses
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Totally Not Frogger")
screen.listen()

# Sets up the PC, cars, and score as entities in the game
avatar = player()
car_manager = carManager()
scoreboard = scoreboard()

# Listens for the player to press up, moving the avatar forward
screen.onkey(avatar.moveUp, "Up")

game_is_on = True
while game_is_on:
    # Sets up the screen to update itself and sets the cars moving
    time.sleep(0.1)
    screen.update()
    car_manager.make_car()
    car_manager.move_cars()
    # Speeds up the cars and increases the score if the player gets to the other side
    if avatar.finish():
        avatar.go_start()
        car_manager.increase_speed()
        scoreboard.score += 1
        scoreboard.update()
    # Checks if the player has been run over by a car and signals a game over if true
    for car in car_manager.cars:
        if car.distance(avatar) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
