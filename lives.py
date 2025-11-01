from turtle import Turtle

class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.goto(150,210)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier",20, "normal"))

    def calculate_lives(self):
        self.lives-=1
        self.update_lives()

