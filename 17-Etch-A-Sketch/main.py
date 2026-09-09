from turtle import Turtle , Screen

timmy = Turtle()


def move_forward():
    timmy.forward(10)


def move_backword():
    timmy.back(10)


def counter_clock_wise():
    timmy.left(20)


def clock_wise():
    timmy.right(20)


def delete_all():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen = Screen()
screen.listen()
screen.onkeypress(key="w",fun=move_forward)
screen.onkeypress(key="s",fun=move_backword)
screen.onkeypress(key="a",fun=counter_clock_wise)
screen.onkeypress(key="d",fun=clock_wise)
screen.onkeypress(key="c",fun=delete_all)

screen.exitonclick()
