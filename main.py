from turtle import Screen, Turtle
from paddle import Paddle

#set up screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Breakout Arcade Game")

#create paddle
paddle = Paddle(0,-200)

#key control
screen.listen()
screen.onkey(paddle.right,key="d")
screen.onkey(paddle.left,key="a")
screen.onkey(paddle.right,key="Right")
screen.onkey(paddle.left,key="Left")

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







screen.mainloop()
