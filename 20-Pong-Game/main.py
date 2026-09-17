from turtle import Screen
from key_paddle import KeyPaddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)


r_paddle = KeyPaddle((350,0))
l_paddle = KeyPaddle((-350,0))
ball = Ball()
score = ScoreBoard()


screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")



is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()


#""walls up and down""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


# ""paddles""
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()




#"""loses"""
    if ball.xcor() > 380:
        ball.reset_pos()
        score.update_score()
        score.r_paddle_score()


    if ball.xcor() <-380:
        ball.reset_pos()
        score.update_score()
        score.l_paddle_score()















screen.exitonclick()
