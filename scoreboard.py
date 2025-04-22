from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.write(f"Score: {self.score}", False, align="center" ,font=("Montserrat", 8,'normal'))

    def writeScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center" ,font=("Montserrat", 8,'normal'))