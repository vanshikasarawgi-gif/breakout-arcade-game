from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200,210)
        self.write(f"{self.score:03d}", align="center", font=("Courier", 20, "normal"))

    def add_points(self, points):
        self.score += points
        self.update_score()


