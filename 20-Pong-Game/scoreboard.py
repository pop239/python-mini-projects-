from turtle import Turtle
FONT = ("Courier" , 80 , "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.hideturtle()
        self.R_score = 0
        self.L_score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.penup()
        self.goto(-100, 200)
        self.write(arg=f"{self.R_score} ", align="center", font=FONT)
        self.goto(100, 200)
        self.write(arg=f"{self.L_score} ", align="center", font=FONT)



    def r_paddle_score(self):
        self.R_score+=1
        self.update_score()


    def l_paddle_score(self):
        self.L_score+=1
        self.update_score()
