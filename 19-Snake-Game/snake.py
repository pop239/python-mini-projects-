from turtle import Turtle
start_pos = [(0, 0), (-20, 0), (-40, 0)]
dis = 20

UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:

    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in start_pos:
            self.add(i)



    def add(self,position):
        new = Turtle(shape="square")
        new.color("white")
        new.penup()
        new.goto(position)
        self.segment.append(new)




    def extent(self):
        self.add(self.segment[-1].position())




    def move(self):

        for seg in range(len(self.segment) - 1, 0, -1):
             x = self.segment[seg - 1].xcor()  # 1 0
             y = self.segment[seg - 1].ycor()  # 1 0
             self.segment[seg].goto(x, y)  # 1,1
        self.head.forward(dis)


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




