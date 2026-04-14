from turtle import *
import random

def generate_random_hex_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def draw_square():
    a = Turtle()
    a.hideturtle()
    a.color("cyan")
    a.speed(0)
    a.begin_fill()
    a.goto(0,300)
    a.goto(300,300)
    a.goto(300,-300)
    a.goto(-300,-300)
    a.goto(-300,300)
    a.goto(0,300)
    a.end_fill()

def move_forward(turtle, turtles):
    turtle.forward(5)

    if turtle.xcor() > 300 or turtle.xcor() < -300:
        turtle.speed(0)
        turtle.setheading(180 - turtle.heading())
        turtle.forward(10)
        turtle.speed(2) 
        new = create_turtle()
        turtles.append(new)
    if turtle.ycor() > 300 or turtle.ycor() < -300:
        turtle.speed(0)
        turtle.setheading(-turtle.heading())
        turtle.forward(10)
        turtle.speed(2)
        new = create_turtle()
        turtles.append(new)
    return turtles

def move_xy(turtle, deltaX, deltaY):
    newX = turtle.xcor() + deltaX
    newY = turtle.ycor() + deltaY

    if newX > 300 or newX < -300:
        deltaX *= -1
        newX = turtle.xcor()
    if newY > 300 or newY < -300:
        deltaY *= -1
        newY = turtle.ycor()

    turtle.goto(newX, newY)
    return deltaX, deltaY

def create_turtle():
    turtle = Turtle()
    turtle.color(generate_random_hex_color())
    turtle.shape("triangle")
    turtle.speed(2)
    turtle.setheading(random.randint(0,360))
    return turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(700,700)

draw_square()

yertle = Turtle()
yertle.color(generate_random_hex_color())
yertle.shape("triangle")
yertle.setheading(random.randint(0,360))
deltaX = random.randint(-5,5)
deltaY = random.randint(-5,5)

turtles = [yertle]

while True:
    for turtle in turtles:
        turtles = move_forward(turtle, turtles)
    


screen.exitonclick()