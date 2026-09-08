               ##       for extracting the color numbers      ##


# import colorgram
# color = []
# colors = colorgram.extract("image.jpg",30)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     tup = (r,g,b)
#     color.append(tup)
#
#
# print(color)



                ##      main project        ##



import turtle as t
import random
timmy = t.Turtle()
t.colormode(255)
timmy.speed(0)
timmy.penup()
timmy.hideturtle() # --> it hides the arrow

color_list = [
    (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
    (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
    (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
    (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208),
    (168, 99, 102)

  ]


timmy.setheading(225)
# timmy.penup()
timmy.forward(300)
timmy.setheading(0)
# timmy.pendown()
def dottt():

    for _ in range(10):

        timmy.dot(20,random.choice(color_list))
        # timmy.penup()
        timmy.forward(50)
        # timmy.pendown()

for _ in range(10):

    dottt()
    timmy.setheading(90)
    # timmy.penup()
    timmy.forward(50)
    # timmy.pendown()
    timmy.setheading(180)
    # timmy.penup()
    timmy.forward(500)
    # timmy.pendown()
    timmy.setheading(0)




screen = t.Screen()
screen.exitonclick()