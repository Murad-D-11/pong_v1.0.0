from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    # Transfers all attributes and methods from the 'Turtle' object into 'Scoreboard' object.
    super().__init__()

    # Default settings of a 'Scoreboard' object.
    self.color("white")
    self.penup()
    self.hideturtle()
    self.p1Score = 0
    self.p2Score = 0
    self.update_scoreboard()

  # Updates the scoreboard.
  def update_scoreboard(self):
    self.clear()
    self.goto(-20, 220)
    self.write(self.p1Score, align="right", font=("Cascadia", 80))
    self.goto(20, 220)
    self.write(self.p2Score, align="left", font=("Cascadia", 80))

  # Increments each players' score.
  def p1_update(self):
    self.p1Score += 1
    self.update_scoreboard()
  
  def p2_update(self):
    self.p2Score += 1
    self.update_scoreboard()

  # Resets the object to its defaults.
  def reset_scoreboard(self):
    self.p1Score = 0
    self.p2Score = 0
    self.update_scoreboard()
