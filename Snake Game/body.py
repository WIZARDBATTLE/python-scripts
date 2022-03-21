from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        super().__init__()
        self.segments = []
        self.snake_start()
        self.head = self.segments[0]
    def snake_start(self):
        for position in STARTING_POSITIONS:
            self.add_piece(position)
    def add_piece(self, position):
        new_piece = Turtle("square")
        new_piece.color("white")
        new_piece.penup()
        new_piece.goto(position)
        self.segments.append(new_piece)
    def grow(self):
        self.add_piece(self.segments[-1].position())
    def move(self):
        for piece in range(len(self.segments)-1,0,-1):
            new_x = self.segments[piece-1].xcor()
            new_y = self.segments[piece-1].ycor()
            self.segments[piece].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)