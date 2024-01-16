
from turtle import Turtle


#CONSTANTS:
ball_speed_modifier = 0.1
AMOUNT_OF_PIXELS_BALL_MOVES_EACH_FRAME = 10

class Ball(Turtle):

    def __init__(self):  # I took out: , ball_position) after self       extras: shape, pensize=20, color="orange"
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.setheading(45)
        # self.goto(ball_position)
        self.x_move = AMOUNT_OF_PIXELS_BALL_MOVES_EACH_FRAME
        self.y_move = AMOUNT_OF_PIXELS_BALL_MOVES_EACH_FRAME
        # self.forward(AMOUNT_OF_PIXELS_BALL_MOVES_EACH_FRAME)
        self.move_speed = ball_speed_modifier      #takes the 0.1 time.sleep modifier and runs math on it to reduce it by about 10% or less each iteration, if it hits a paddle.
                #goes from 0.1 to 0.09 to 0.081, etc.. the lower number causes shorter time delay to occur between annimation frames, causing the ball to move faster!

    def move(self):
        # self.forward(AMOUNT_OF_PIXELS_SNAKE_MOVES_EACH_FRAME)
        #or
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_off_y_vertical_walls(self):
        self.y_move *= -1    #inverts the negativity or positivity of a value.

    def bounce_off_x_axis_paddle(self):
        self.x_move *= -1    #reverses ONLY the x-axis trajectory (makes the ball bounce off of the paddles and goes the other way in the x-axis, but continues the same for y-axis)
        self.move_speed *= 0.9  #increases in speed (by about 10%?)


    def reset_position(self):
        self.goto(0, 0)        #resets location for ball to start after ball gets missed.
        # self.x_move *= -1
        self.move_speed = ball_speed_modifier #this way, when it goes out of bounds, it resets the speed of the ball back to the original amount, which is ball_speed_modifier
        self.bounce_off_x_axis_paddle      #this runs the function and inverts the x-direction after a paddle misses the ball.