import turtle

def grid():
    turtle.speed(10)
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


def x(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(45)
    turtle.pencolor("red")
    turtle.down()

    turtle.forward(40)
    turtle.backward(80)
    turtle.forward(40)

    turtle.left(90)

    turtle.forward(40)
    turtle.backward(80)


def o(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(0)

    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.backward(40)

    turtle.pencolor("blue")
    turtle.down()
    turtle.circle(40)


grid()

x(0, 0)
o(0, 0)

turtle.done()