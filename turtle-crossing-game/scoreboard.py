from turtle import Turtle
ALIGNMENT = 'left'
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x, y)
        self.color("black")
        self.hideturtle()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)
