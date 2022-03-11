from turtle import Screen
from Paddle import paddle
from Ball import ball
from Scoreboard import scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)

rightPaddle = paddle((350, 0))
leftPaddle = paddle((-350, 0))
ball = ball()
scoreboard = scoreboard()

screen.listen()
screen.onkey(rightPaddle.goUp, "Up")
screen.onkey(rightPaddle.goDown, "Down")
screen.onkey(leftPaddle.goUp, "w")
screen.onkey(leftPaddle.goDown, "s")

gameIsOn = True
sleepTime = 0.1
while gameIsOn:
    time.sleep(sleepTime)
    if sleepTime > 0.05:
        sleepTime -= 0.01
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
    if ball.distance(rightPaddle) < 50 and ball.xcor() > 320 or ball.distance(leftPaddle) < 50 and ball.xcor() < -320:
        print("contact")
        ball.bounceX()
    if ball.xcor() > 380:
        ball.point()
        scoreboard.leftPoint()
    elif ball.xcor() < -380:
        ball.point()
        scoreboard.rightPoint()
    scoreboard.scoreboardUpdate()
screen.exitonclick()
