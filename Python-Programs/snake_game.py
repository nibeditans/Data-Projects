# Importing pakages
import turtle
import random
import time


# Creating screen
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=800, height=700)
screen.tracer(0)
screen.bgcolor("black")

# Creating Boarder
turtle.speed(5)
turtle.pensize(7)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("yellow")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# Score
score = 0
delay = 0.1

# Snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("yellow")
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

# Scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("green")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("score:", align="center", font=("Courier", 24, "bold"))

# Defining how to move
def snake_go_up():
    if snake.direction != "Down":
        snake.direction = "Up"

def snake_go_down():
    if snake.direction != "Up":
        snake.direction = "Down"

def snake_go_left():
    if snake.direction != "Right":
        snake.direction = "Left"

def snake_go_right():
    if snake.direction != "Left":
        snake.direction = "Right"

def snake_move():
    if snake.direction == "Up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "Down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "Left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "Right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard Binding
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")


# Main Loop
while True:
    screen.update()

    # Snake and Fruit Collision
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("score: {}".format(score), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001

        # Creating New Food
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("yellow")
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # Adding ball to the Snake
    for index in range(len(old_fruit) -1, 0, -1):
        a = old_fruit[index -1].xcor()
        b = old_fruit[index -1].ycor()

        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
         a = snake.xcor()
         b = snake.ycor()
         old_fruit[0].goto(a, b)
    snake_move()

    # Snake and Boarder Collision
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("yellow")
        scoring.goto(0, 0)
        scoring.write("     Game Over \n Your Score is {}".format(score), align="center", font=("Courier", 30, "bold"))

    # Snake itself Collision
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("green")
            scoring.goto(0, 0)
            scoring.write("    Game Over \n Your Score is {}".format(score), align="center",
                          font=("Courier", 30, "bold"))

    time.sleep(delay)

turtle.Terminator()
