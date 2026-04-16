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
    turtle.pensize(3)
    turtle.setheading(random.randint(0,360))
    return turtle

def create_player():
    global player
    player = Turtle()
    player.speed(0)
    player.shape("square")
    player.color("white")
    player.pensize(3)

def up():
    global player
    player.sety(player.ycor() + 5)

def down():
    global player
    player.sety(player.ycor() - 5)

def left():
    global player
    player.setx(player.xcor() - 5)

def right():
    global player
    player.setx(player.xcor() + 5)





screen = Screen()
screen.bgcolor("black")
screen.setup(700,700)

screen.listen()
screen.onkeypress(create_player, "space")
screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")

draw_square()

yertle = Turtle()
yertle.color(generate_random_hex_color())
yertle.shape("triangle")
yertle.pensize(3)
yertle.setheading(random.randint(0,360))
deltaX = random.randint(-5,5)
deltaY = random.randint(-5,5)

player = None

turtles = [yertle]

while True:
    for turtle in turtles:
        turtles = move_forward(turtle, turtles)
        if player != None and player.distance(turtle) < 20:
            turtle.hideturtle()
            turtles.remove(turtle)
    


screen.exitonclick()
#