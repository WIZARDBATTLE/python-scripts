from turtle import Turtle
import random

# Constants to be used later
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class carManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    # Makes cars at random on the screen
    def make_car(self):
        car_chance = random.randint(1,6)
        if car_chance == 6:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)
    # Moves the cars forward according to the score
    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)
    # Increases the speed of the cars when the player reaches the end
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT