from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial" , 24 , "normal")
class ScoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.your_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.updated_score()


    def updated_score(self):
        self.write(arg=f"score:{self.your_score} ",align= ALIGNMENT, font=FONT)


    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(arg="Game Over" , align=ALIGNMENT , font=FONT)


    def track(self):
        self.your_score+=1
        self.clear()
        self.updated_score()
