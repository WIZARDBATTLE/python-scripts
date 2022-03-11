from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.rightScore = 0
        self.leftScore = 0
        self.goto(100, 150)
        self.write(self.rightScore, align="center", font=("courier", 80, "normal"))
        self.goto(-100, 150)
        self.write(self.leftScore, align="center", font=("courier", 80, "normal"))

    def scoreboardUpdate(self):
        self.clear()
        self.goto(100, 150)
        self.write(self.rightScore, align="center", font=("courier", 80, "normal"))
        self.goto(-100, 150)
        self.write(self.leftScore, align="center", font=("courier", 80, "normal"))

    def rightPoint(self):
        self.rightScore += 1
    def leftPoint(self):
        self.leftScore += 1