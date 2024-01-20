import turtle
t = turtle.Turtle()
screen = turtle.Screen()
t.pensize(4)
switch = 0
graphic_size = 252
r4 = (11 / 12) * graphic_size
r3 = (10 / 12) * graphic_size
r2 = (9 / 12) * graphic_size
r1 = (4 / 12) * graphic_size

def circle(x):
    t.fillcolor()
    t.begin_fill()
    t.circle(x)
    t.end_fill()

def bar(y):
    t.begin_fill()
    for i in range(2):
        t.forward((4 / 3) * y)
        t.left(90)
        t.forward((1 / 9) * y)
        t.left(90)
    t.end_fill()

def gap(z):
    t.begin_fill()
    for i in range(4):
        t.forward((1 / 6) * z)
        t.left(90)
    t.end_fill()

t.penup()
for radius in [graphic_size, r4, r3, r2, r1]:
    t.forward(radius)
    t.left(90)
    t.pendown()
    circle(radius)
    t.penup()
    t.home()
    if switch == 0:
        t.color("white")
        switch = 1
        continue
    t.color("black")
    switch = 0

t.color("black")
for angle in [0, 45, 90, 135]:
    t.left(angle)
    t.backward((2 / 3) * graphic_size)
    t.right(90)
    t.forward((1 / 18) * graphic_size)
    t.left(90)
    t.pendown()
    bar(graphic_size)
    t.penup()
    t.home()

t.color("white")
for i in range(8):
    t.right(90)
    t.forward((1 / 12) * graphic_size)
    t.left(90)
    t.forward((178.5 / 252) * graphic_size)
    t.pendown()
    gap(graphic_size)
    t.penup()
    t.home()
    t.left((1 + i) * 45)

t.hideturtle()
screen.exitonclick()
