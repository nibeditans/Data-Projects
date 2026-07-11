import turtle

ninja = turtle.Turtle()

ninja.speed(100)
ninja.color('Green')

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    ninja.pendown()

    ninja.write("NS", font=['Bold', 20])

    ninja.penup()
    ninja.setposition(0, 1)
    ninja.pendown()
    ninja.color('Green')
    ninja.goto(-70, 70)
    ninja.right(2)
    ninja.color('Green')

turtle.done()
