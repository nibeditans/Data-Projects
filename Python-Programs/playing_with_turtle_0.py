import turtle

# create a turtle object
t = turtle.Turtle()


# creating the screen
screen = turtle.Screen()
screen.bgcolor("Black")


# set the turtle's speed
t.speed(0)


# draw the first circle
t.penup()
t.goto(0, -100)
t.pendown()
t.begin_fill()
t.color("Green")
t.circle(180)
t.end_fill()


t.penup()
t.goto(0, -100)
t.pendown()
t.color("Yellow")
t.circle(170)
t.circle(160)
t.circle(150)
t.circle(140)
t.circle(130)
t.circle(120)
t.circle(110)
t.circle(100)
t.circle(90)
t.circle(80)
t.circle(70)
t.circle(60)
t.circle(50)
t.circle(40)
t.circle(30)
t.circle(20)
t.circle(10)


t.penup()
t.goto(0, -100)
t.pendown()
t.color("Red")
t.circle(5)
t.circle(15)
t.circle(25)
t.circle(35)
t.circle(45)
t.circle(55)
t.circle(65)
t.circle(75)
t.circle(85)
t.circle(95)
t.circle(105)
t.circle(115)
t.circle(125)
t.circle(135)
t.circle(145)
t.circle(155)
t.circle(165)
t.circle(175)
t.circle(185)


# draw the 2nd circle
t.penup()
t.goto(0, -100)
t.pendown()
t.begin_fill()
t.color("Yellow")
t.circle(-75)
t.end_fill()


t.penup()
t.goto(0, -100)
t.pendown()
t.color("Green")
t.circle(-65)
t.circle(-55)
t.circle(-45)
t.circle(-35)
t.circle(-25)
t.circle(-15)
t.circle(-5)


t.penup()
t.goto(0, -100)
t.pendown()
t.color("Green")
t.circle(-65)
t.circle(-55)
t.circle(-45)
t.circle(-35)
t.circle(-25)
t.circle(-15)
t.circle(-5)


t.penup()
t.goto(0, -100)
t.pendown()
t.color("Red")
t.circle(-10)
t.circle(-20)
t.circle(-30)
t.circle(-40)
t.circle(-50)
t.circle(-60)
t.circle(-70)
t.circle(-80)


# keep the window open until closed manually
turtle.done()
