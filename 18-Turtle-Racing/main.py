import random
from turtle import Turtle , Screen

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Entre a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos=[-100, -50 , 0 , 50 , 100 , 150]
turtles=[]

for i in range(6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for t in turtles:
        if t.xcor() > 230:
            is_race_on=False
            wining_color = t.pencolor() # --> return 1 color 

            if wining_color == user_bet:
                print(f"you've won! the {wining_color} turtle is the winner")

            else:
                print(f"you've lose! the {wining_color} turtle is the winner")

        random_dis=random.randint(0,10)
        t.forward(random_dis)



screen.exitonclick()