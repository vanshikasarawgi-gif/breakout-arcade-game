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







screen.mainloop()
