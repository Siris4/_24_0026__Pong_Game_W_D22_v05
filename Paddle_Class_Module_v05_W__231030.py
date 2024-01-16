
from turtle import Turtle

STARTING_POSITIONS = [(0, -20), (0, 0), (0, 20), (0, 40)]    #will ALWAYS start here, so using Tuples is PERFECT!! Constants = Tuples, so this goes in ALL CAPS!
# AMOUNT_OF_PIXELS_SNAKE_MOVES_EACH_FRAME = 20
#to prevent from cheating and doing a 180 turn:
UP = 90
DOWN = 270
# LEFT = 180
# RIGHT = 0


class Paddle(Turtle):
    
    def __init__(self, position):           # extras: shape, pensize=20, color="orange"
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
