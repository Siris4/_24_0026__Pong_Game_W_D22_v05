
from turtle import Turtle
# from __2x__Pong_Game_Main_v02_W__231027 import p1_scoreboard_location, p2_scoreboard_location

#CONSTANTS:
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):    # , p1_scoreboard) removed
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.r_p1_score = 0
        self.l_p2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(100, 270)
        # self.write_the_scoreboard_for_p1()
        self.write(f"P1 Score: {self.r_p1_score}", align=ALIGNMENT, font=("Courier", 16, "normal"))
        self.goto(-100, 270)
        self.write(f"P2 Score: {self.l_p2_score}", align=ALIGNMENT, font=("Courier", 16, "normal"))
        # self.write_the_scoreboard_for_p2()

    def l_point(self):
        self.l_p2_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_p1_score += 1
        self.update_scoreboard()
    