from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Courier New", 24, "bold"))

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier New", 24, "bold"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier New", 24, "bold"))
        