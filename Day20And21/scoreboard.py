
from turtle import Turtle

class Scoreboard(Turtle):
    
    
    
    def read_high_score(self): 
        high_score = 0
        with open("highscore.txt") as file:
            content = file.read().strip()
            high_score = int(content)
        return high_score
            
    def write_high_score(self, score):
        with open("highscore.txt", "w") as file:
            file.write(str(score))

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()
        
    def reset(self):
        if self.score > self.high_score:
            self.write_high_score(self.score)
            self.high_score = self.read_high_score()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def updateScore(self):
        self.score += 1
        self.update_scoreboard()