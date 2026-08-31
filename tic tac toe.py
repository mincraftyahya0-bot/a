import turtle
def draw_x(x, y):
    turtle.up()
    turtle.goto(x - 30, y - 30)
    turtle.down()
    turtle.goto(x + 30, y + 30)

    turtle.up()
    turtle.goto(x - 30, y + 30)
    turtle.down()
    turtle.goto(x + 30, y - 30)

import turtle

def draw_o(x, y):
    turtle.up()
    turtle.goto(x, y - 30)
    turtle.down()
    turtle.circle(30)

def clicked(x, y):
    draw_o(x, y)

turtle.onscreenclick(clicked)

turtle.done()

'''turtle.speed(3)
turtle.pensize(4)

turtle.up()
turtle.goto(-50, 150)
turtle.down()
turtle.goto(-50, -150)

turtle.up()
turtle.goto(50, 150)
turtle.down()
turtle.goto(50, -150)

turtle.up()
turtle.goto(-150, 50)
turtle.down()
turtle.goto(150, 50)

turtle.up()
turtle.goto(-150, -50)
turtle.down()
turtle.goto(150, -50)

turtle.hideturtle()
turtle.done()'''
