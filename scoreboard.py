from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("score.txt") as data:
            file_score=int(data.read())
            self.high_score = file_score
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def high_score_update(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            try:
                with open(f"score.txt", "w") as data:
                    data.write(f"{self.high_score}")
                    print(" High Score Updated")
            except (FileNotFoundError, ValueError):
                self.high_score = 0

    def reset_score(self):
        self.high_score_update()
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.high_score_update()
        self.update_scoreboard()

