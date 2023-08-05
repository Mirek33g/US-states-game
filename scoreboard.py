from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("black")
    self.penup()
    self.goto(0, 250)
    self.hideturtle()
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"{self.score} / 50 States",
               align=ALIGMENT,
               font=FONT)

  #def reset(self):
   # if self.score > self.high_score:
   #   self.high_score = self.score
   # self.score = 0
  #  self.update_scoreboard()

  def increase_score(self):
    self.score += 1
    self.update_scoreboard()