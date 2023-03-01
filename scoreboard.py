from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


# TODO 5. Create a scoreboard

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.setposition(0, 275)
        self.hideturtle()
        self.pencolor("white")
        self.score = 0
        self.display()

    def display(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align='center', font=FONT)
