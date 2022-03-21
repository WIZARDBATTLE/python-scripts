from turtle import Turtle

FONT = ("Oswald", 24, "bold")
ALIGNMENT = "center"


class scoreboard(Turtle):
    # Sets up the scoreboard on screen
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.score = 0
        self.penup()
        self.goto(-220, 260)
        self.update()
    # Updates the scoreboard with the current score
    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
    # The game over "sequence"
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)