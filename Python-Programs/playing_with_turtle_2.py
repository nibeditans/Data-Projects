import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("Black")
t.hideturtle()
t.goto(0, -10)

t.pensize(7)
t.color("Red")
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-115, 90)
t.pendown()
t.color("Black")
t.write("I Love You!", font=['Bold', 40])

t.penup()
t.goto(-100, -100)
t.pendown()
t.color("White")
t.write("Created By NS", font=['Arial', 25])

turtle.done()
