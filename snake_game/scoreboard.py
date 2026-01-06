from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier New", 24, "bold"))

    def increase_score(self):
        self.score+=1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=("Courier New", 24, "bold"))
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()