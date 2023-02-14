from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 17, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:\\Users\\Edson\\Documents\GitHub\\pythontraining\day21\\snake_game\\data.txt", "r") as f:
            self.high_score = int(f.read())
            print(self.high_score)
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score = {self.score} High Score = {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("C:\\Users\\Edson\\Documents\GitHub\\pythontraining\day21\\snake_game\\data.txt", "w") as f:
                f.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
