from turtle import *

def regular_polygon(turtle, sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(400/sides)
        turtle.right(360/sides)
    turtle.end_fill()


screen = Screen()
screen.bgcolor("silver")

pen = Turtle()
pen.speed(0)
pen.color("purple")
pen.hideturtle()

name = Turtle()
name.ht
name.speed(0)

while True:
    sides = int(input("How many sides?"))
    pen.clear()
    if sides == 3:
        regular_polygon(pen, sides)
        name.write("TRIANGLE", font = ("Times New Roman", 20))
    elif sides == 5:
            regular_polygon(pen, sides)
            name.write("PENTAGON", font = ("Times New Roman", 20))
    elif sides == 6:
            regular_polygon(pen, sides)
            name.write("HEXAGON", font = ("Times New Roman", 20))
    elif sides == 4:
        regular_polygon(pen, sides)
        name.write("QUADRILATERAL", font = ("Times New Roman", 20))
    else:
        regular_polygon(pen, sides)
        regular_polygon(pen, sides)
        name.write("HEXAGON", font = ("Times New Roman", 20))


screen.exitonclick()