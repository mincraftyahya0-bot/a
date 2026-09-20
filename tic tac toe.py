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


def x(place):
    if place == "middle":
        x = 0
        y = 0
    elif place == "top_left":
        x = -100
        y = 100
    elif place == "top_middle":
        x = 0
        y = 100
    elif place == "top_right":
        x = 100
        y = 100
    elif place == "middle_left":
        x = -100
        y = 0
    elif place == "middle_right":
        x = 100
        y = 0
    elif place == "bottom_left":
        x = -100
        y = -100
    elif place == "bottom_middle":
        x = 0
        y = -100
    elif place == "bottom_right":
        x = 100
        y = -100
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


def o(place):
    if place == "middle":
        x = 0
        y = 0
    elif place == "top_left":
        x = -100
        y = 100
    elif place == "top_middle":
        x = 0
        y = 100
    elif place == "top_right":
        x = 100
        y = 100
    elif place == "middle_left":
        x = -100
        y = 0
    elif place == "middle_right":
        x = 100
        y = 0
    elif place == "bottom_left":
        x = -100
        y = -100
    elif place == "bottom_middle":
        x = 0
        y = -100
    elif place == "bottom_right":
        x = 100
        y = -100
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
while True:
    player1= input("enter your player (x/o):")
    player2= "o" if player1 == "x" else "x"
    place1 = input("enter your place (top_left, top_middle, top_right, middle_left, middle, middle_right, bottom_left, bottom_middle, bottom_right):")
    place2 = input("enter your place (top_left, top_middle, top_right, middle_left, middle, middle_right, bottom_left, bottom_middle, bottom_right):")
    if player1 == "x":
        x(place1)
    elif player1 == "o":
        o(place1)
    if player2 == "x":
        x(place2)
    elif player2 == "o":
        o(place2)

    win1 = True if player1 == "x" and ((place1 == "top_left" and place2 == "top_middle" and place2 == "top_right") or (place1 == "middle_left" and place2 == "middle" and place2 == "middle_right") or (place1 == "bottom_left" and place2 == "bottom_middle" and place2 == "bottom_right") or (place1 == "top_left" and place2 == "middle_left" and place2 == "bottom_left") or (place1 == "top_middle" and place2 == "middle" and place2 == "bottom_middle") or (place1 == "top_right" and place2 == "middle_right" and place2 == "bottom_right") or (place1 == "top_left" and place2 == "middle" and place2 == "bottom_right") or (place1 == "top_right" and place2 == "middle" and place2 == "bottom_left")) else False
    win2 = True if player2 == "x" and ((place1 == "top_left" and place2 == "top_middle" and place2 == "top_right") or (place1 == "middle_left" and place2 == "middle" and place2 == "middle_right") or (place1 == "bottom_left" and place2 == "bottom_middle" and place2 == "bottom_right") or (place1 == "top_left" and place2 == "middle_left" and place2 == "bottom_left") or (place1 == "top_middle" and place2 == "middle" and place2 == "bottom_middle") or (place1 == "top_right" and place2 == "middle_right" and place2 == "bottom_right") or (place1 == "top_left" and place2 == "middle" and place2 == "bottom_right") or (place1 == "top_right" and place2 == "middle" and place2 == "bottom_left")) else False
    if win1:
        print("player 1 wins!")
        break
    elif win2:
        print("player 2 wins!")
        break
turtle.done()