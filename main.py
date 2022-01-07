import turtle  # import turtle for the screen

# here is the screen properties
wind = turtle.Screen()  # initialize screen
wind.title("NorahPingPong")  # screen title
wind.bgcolor("gray")  # screen background color
wind.setup(width=800, height=600)  # screen dimension
wind.tracer(0)  # stop the window automatically updating

# right paddle
rightPaddle = turtle.Turtle()  # initialize turtle object(shape)
rightPaddle.speed(0)  # set the speed of the animation
rightPaddle.shape("square")  # set rightPaddle shape
rightPaddle.color("blue")  # set rightPaddle color
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)  # stretch the length and width for rightPaddle
rightPaddle.penup()  # rightPaddle do not draw lines when it is moving
rightPaddle.goto(350, 0)  # set rightPaddle position

# left paddle
leftPaddle = turtle.Turtle()  # initialize turtle object(shape)
leftPaddle.speed(0)  # set the speed of the animation
leftPaddle.shape("square")  # set leftPaddle shape
leftPaddle.color("red")  # set leftPaddle color
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)  # stretch the length and width for leftPaddle
leftPaddle.penup()  # leftPaddle do not draw lines when it is moving
leftPaddle.goto(-350, 0)  # set leftPaddle position

# the ball
ball = turtle.Turtle()  # initialize turtle object(shape)
ball.speed(0)  # set the speed of the animation
ball.shape("circle")  # set ball shape
ball.color("black")  # set ball color
ball.penup()  # ball do not draw lines when it is moving
ball.goto(0, 0)  # set ball position
ball.dx = 0.10  # everytime the ball moving x coordinate increase 2.5
ball.dy = 0.10  # everytime the ball moving y coordinate increase 2.5

# score
RedPlayerScore = 0  # initial value for the RedPlayerScore
BluePlayerScore = 0  # initial value for the BluePlayerScore
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()  # just show what is writing in this object
score.goto(0, 260)
score.write("RedPlayer: 0 BluePlayer:0 ", align="center", font=("Courier", 24, "bold"))

# functions
def rightPaddle_up():
    y = rightPaddle.ycor()  # return the y coordinate for the rightPaddle
    y += 20  # plus 20 pxl for the y coordinate so the rightPaddle going up
    rightPaddle.sety(y)  # set the new y after plus 20 pxl to the rightPaddle

def rightPaddle_down():
    y = rightPaddle.ycor()  # return the y coordinate for the rightPaddle
    y -= 20  # plus 20 pxl for the y coordinate so the rightPaddle going down
    rightPaddle.sety(y)  # set the new y after plus 20 pxl to the rightPaddle

def leftPaddle_up():
    y = leftPaddle.ycor()  # return the y coordinate for the leftPaddle
    y += 30  # plus 20 pxl for the y coordinate so the leftPaddle going up
    leftPaddle.sety(y)  # set the new y after plus 20 pxl to the leftPaddle

def leftPaddle_down():
    y = leftPaddle.ycor()  # return the y coordinate for the leftPaddle
    y -= 30  # plus 20 pxl for the y coordinate so the leftPaddle going down
    leftPaddle.sety(y)  # set the new y after plus 20 pxl to the leftPaddle

# keyboard bindings
wind.listen()  # tell the window to expect keyboard input
wind.onkeypress(rightPaddle_up, "Up")  # if  "Up" pressed start rightPaddle_up()
wind.onkeypress(rightPaddle_down, "Down")  # if  "Down" pressed start rightPaddle_down()
wind.onkeypress(leftPaddle_up, "w")  # if  "w" pressed start leftPaddle_up()
wind.onkeypress(leftPaddle_down, "s")  # if  "s" pressed start leftPaddle_down()

# game loop
while True:
    wind.update()  # update the screen everytime the loop run

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)  # ball start at 0 and everytime loops run plus 0.5 to x-axis
    ball.sety(ball.ycor() + ball.dy)  # ball start at 0 and everytime loops run plus 0.5 to y-axis

    # border check  (the top is 300px) (the bottom is -300px) (right is 400px) (left is -400px) (ball is 20px)
    if ball.ycor() > 290:  # if the ball go up and hit the border
        ball.sety(290)  # set y coordinate for the ball at 290
        ball.dy *= -1  # let the ball reverse the direction

    if ball.ycor() < -290:  # if the ball go down and hit the border
        ball.sety(-290)  # set y coordinate for the ball at -290
        ball.dy *= -1  # let the ball reverse the direction

    if ball.xcor() > 390:  # if the ball go right and hit the border
        ball.goto(0, 0)  # return the ball to the center (game over)
        ball.dx *= -1  # let the ball reverse the direction
        RedPlayerScore += 1  # increase the score +1 for RedPlayer
        score.clear()  # clear the score everytime to put the new score
        score.write("RedPlayer:{} BluePlayer:{} ".format(RedPlayerScore, BluePlayerScore), align="center", font=("Arial", 22, "bold"))

    if ball.xcor() < -390:  # if the ball go left and hit the border
        ball.goto(0, 0)  # return the ball to the center (game over)
        ball.dx *= -1  # let the ball reverse the direction
        BluePlayerScore += 1  # increase the score +1 for BluePlayer
        score.clear()  # clear the score everytime to put the new score
        score.write("RedPlayer:{} BluePlayer:{} ".format(RedPlayerScore, BluePlayerScore), align="center", font=("Arial", 22, "bold"))

    # if the ball hit the rightPaddle
    if (340 < ball.xcor() < 350) and (rightPaddle.ycor() + 40 > ball.ycor() > rightPaddle.ycor() - 40):
        ball.setx(340)  # set the ball at 340 x-axis
        ball.dx *= -1  # let the ball reverse the direction

    # if the ball hit the leftPaddle
    if (-340 > ball.xcor() > -350) and (leftPaddle.ycor() + 40 > ball.ycor() > leftPaddle.ycor() - 40):
        ball.setx(-340)  # set the ball at -340 x-axis
        ball.dx *= -1  # let the ball reverse the direction

