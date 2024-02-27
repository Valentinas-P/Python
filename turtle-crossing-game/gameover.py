from turtle import Turtle
ALIGNMENT = 'center'
FONTNAME = ('Courier', 15, 'normal')


class GameOver(Turtle):

    def __init__(self):
        super().__init__()

        self.color("red")
        self.hideturtle()
        self.penup()

    def game_over(self):
        self.write("Game Over.", align=ALIGNMENT, font=FONTNAME)
