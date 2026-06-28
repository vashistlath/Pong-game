import turtle


# Screen Setup
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle 1
pad1 = turtle.Turtle()
pad1.speed(0)
pad1.shape("square")
pad1.color("white")
pad1.penup()
pad1.shapesize(stretch_wid=5, stretch_len=1)
pad1.goto(-350, 0)

# Paddle 2
pad2 = turtle.Turtle()
pad2.speed(0)
pad2.shape("square")
pad2.color("white")
pad2.penup()
pad2.shapesize(stretch_wid=5, stretch_len=1)
pad2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# Score display — outside the loop!
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Paddle Movement
def pad1up():
    y = pad1.ycor()
    if y < 250:
        pad1.sety(y + 50)

def pad1down():
    y = pad1.ycor()
    if y > -250:
        pad1.sety(y - 50)

def pad2up():
    y = pad2.ycor()
    if y < 250:
        pad2.sety(y + 50)

def pad2down():
    y = pad2.ycor()
    if y > -250:
        pad2.sety(y - 50)

# Keyboard Bindings
wn.listen()
score1 = 0
score2 = 0

wn.onkey(pad1up, "w")
wn.onkey(pad1down, "s")
wn.onkey(pad2up, "Up")
wn.onkey(pad2down, "Down")

# Main Game Loop
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Bottom wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right edge (player 1 scores)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -1
        ball.dy = 1
        score1 += 1

    # Left edge (player 2 scores)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = 1
        ball.dy = 1
        score2 += 1

    # Left paddle collision
    if -345 < ball.xcor() < -330 and pad1.ycor() - 50 < ball.ycor() < pad1.ycor() + 50:
        ball.setx(-330)
        ball.dx *= -1

    # Right paddle collision
    if 330 < ball.xcor() < 345 and pad2.ycor() - 50 < ball.ycor() < pad2.ycor() + 50:
        ball.setx(330)
        ball.dx *= -1

    # Update score
    pen.clear()
    pen.write(
        f"Player 1: {score1}    Player 2: {score2}",
        align="center",
        font=("Courier", 24, "normal")
    )