import time
from turtle import Screen, Turtle
from paddle import Paddle
from bricks import Bricks
from ball import Ball

#set up screen
turtle = Turtle()
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Breakout Arcade Game")
screen.tracer(0) #turn off animation

#create paddle
paddle = Paddle(0,-250)

#key control
screen.listen()
screen.onkeypress(paddle.right,key="d")
screen.onkeypress(paddle.left,key="a")
screen.onkeypress(paddle.right,key="Right")
screen.onkeypress(paddle.left,key="Left")

#create bricks
colors = ["red","orange","green","yellow"]
bricks_list = []
y_start = 200
for row in range(8):
    color = colors[row//2]  #floor div divides and round it to nearest whole number (towards negative) eg 1.5 = 1, 0.5 =0
    y = y_start - row *20
    for x in range(-300,350,50):
        new_brick = Bricks(color,(x,y))
        bricks_list.append(new_brick)

#create ball
ball = Ball()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #detect collisions with top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    #detect collisions with side wall
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    #detect collisions with paddle
    if ball.distance(paddle)<50 and ball.ycor()<-230:
        ball.sety(-230)  #move ball just above the paddle
        ball.bounce_y()

    #detect collisions with bricks
    for brick in bricks_list:
        if ball.distance(brick)<30:
            ball.bounce_y()
            bricks_list.remove(brick)
            brick.hideturtle()

            # check which side is closer
            if abs(ball.xcor() - brick.xcor()) > abs(ball.ycor() - brick.ycor()):
                ball.bounce_x()  # side hit
            else:
                ball.bounce_y()  # top/bottom hit

            player_score.player_score()
            break

screen.exitonclick()
