import turtle


def square(side):
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)


def rectangle(side):
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)


def equilateral_triangle(side):
    turtle.forward(side)
    turtle.left(180-60)
    turtle.forward(side)
    turtle.left(180-60)
    turtle.forward(side)
    turtle.left(180-60)
