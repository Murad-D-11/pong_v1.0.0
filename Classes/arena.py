from turtle import Turtle

class Setup(Turtle):
  def __init__(self, heading, position):
    # Transfers all attributes and methods from the 'Turtle' object into 'Setup' object.
    super().__init__()

    # Default settings of a 'Setup' object.
    self.hideturtle()
    self.penup()
    self.setheading(heading)
    self.pencolor("white")
    self.goto(position)

  # Draws a dividing line.
  def draw_line(self):
    self.pendown()
    self.forward(740)

  # Draws a circle. 
  def draw_circle(self, radius):
    self.pendown()
    self.circle(radius)
