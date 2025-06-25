from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position):
    # Transfers all attributes and methods from the 'Turtle' object into 'Paddle' object.
    super().__init__()

    # Default settings of a 'Paddle' object.
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.penup()
    self.setpos(position)

  # Lets the paddle ascend.
  def up(self):
    if self.ycor() + 10 < 320:
      newY = self.ycor() + 10
      self.goto(y=newY, x=self.xcor())

  # Lets the paddle descend.
  def down(self):
    if self.ycor() - 10 > -320:
      newY = self.ycor() - 10
      self.goto(y=newY, x=self.xcor())

  # Resets the object to its defaults.
  def reset_paddle(self, position):
    self.setpos(position)