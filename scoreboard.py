from turtle import Turtle

FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,250)
        self.update_score()
        self.color("black")
        self.hideturtle()

    def update_score(self):
        self.write(f"Score:{self.score}", font= FONT, align="center")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.write("Juego terminado por malo:(", font= FONT, align="center")