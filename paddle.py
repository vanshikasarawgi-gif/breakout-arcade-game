from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_position,y_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=4)  #horizontal paddle
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.goto(x=x_position,y=y_position)

    def right(self):
        x_cor = self.xcor() +20
        self.goto(x_cor,self.ycor())

    def left(self):
        x_cor = self.xcor() - 20
        self.goto(x_cor,self.ycor())





