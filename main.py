from turtle import Screen, Turtle
from paddle import Paddle

#set up screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Breakout Arcade Game")

#create paddle
paddle = Paddle(0,-200)








screen.mainloop()
