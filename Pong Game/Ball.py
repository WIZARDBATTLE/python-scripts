from turtle import Turtle


class ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.xMove = 10
        self.yMove = 10

    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX, newY)

    def bounceY(self):
        self.yMove *= -1

    def bounceX(self):
        self.xMove *= -1

    def point(self):
        self.goto(0,0)
        self.bounceX()
