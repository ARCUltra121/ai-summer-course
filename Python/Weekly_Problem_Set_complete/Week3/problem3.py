import turtle
import random


def draw_sun(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()


def draw_rectangle(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.begin_fill()

    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.end_fill()


def draw_pond(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.setheading(0)
    
    for i in range(2):
        t.circle(80, 90)
        t.circle(40, 90)

    t.end_fill()


def draw_tree(t, x, y, height):
    trunk_width = 20
    draw_rectangle(t, x, y, trunk_width, height, "brown")
    t.penup()
    t.goto(x + trunk_width / 2, y + height)
    t.pendown()

    t.color("green")
    t.begin_fill()
    t.circle(35)
    t.end_fill()


t = turtle.Turtle()
t.speed(0)

screen = turtle.Screen()
screen.title("Drawing")
screen.bgcolor("skyblue")

draw_sun(t, -300, 180)

draw_rectangle(t, -400, -250, 800, 150, "green")

draw_pond(t, 100, -220)

for _ in range(10):
    x = random.randint(-350, 300)

    height = random.randint(40, 100)

    y = -100

    draw_tree(t, x, y, height)


t.hideturtle()
turtle.done()