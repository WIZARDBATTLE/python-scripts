from turtle import Turtle

# Constants to be used later
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class player(Turtle):
    def __init__(self):
        # Sets up the avatar on the screen
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.go_start()
    # Moves the player forward
    def moveUp(self):
        self.forward(MOVE_DISTANCE)
    # Returns the player to the start
    def go_start(self):
        self.goto(STARTING_POSITION)
    # Signals if the player has reached the other side
    def finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False