import turtle as tu

screen = tu.Screen()
tu.speed(10)

def move_forward():
    tu.forward(10)

def move_backward():
    tu.forward(10)

def turn_left():
    new_heading = tu.heading()+10
    tu.setheading(new_heading)

def turn_right():
    new_heading = tu.heading() - 10
    tu.setheading(new_heading)

def clear():
    tu.clear()
    tu.home()


screen.listen()
screen.onkey(move_forward,'w')
screen.onkey(move_backward,'s')
screen.onkey(turn_left,'a')
screen.onkey(turn_right,'d')
screen.onkey(clear,'q')
screen.exitonclick()



