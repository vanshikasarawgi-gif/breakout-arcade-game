from turtle import Turtle

class Bricks(Turtle):
    def __init__(self,color,position):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=0.5,stretch_len=2)
        self.penup()
        self.speed("fastest")
        self.goto(position)


