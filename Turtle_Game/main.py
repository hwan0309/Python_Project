import turtle as tu
import random

tu.colormode(255)
tim = tu.Turtle()
tim.speed(10)
tim.penup()
tim.hideturtle()
color_list=[(202,164,109),(238,240,245),(150,75,49),(223,201,135),(52,93,135),(172,154,40),(140,30,19)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)