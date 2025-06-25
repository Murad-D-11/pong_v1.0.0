from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    # Transfers all attributes and methods from the 'Turtle' object into 'Ball' object.
    super().__init__()

    # Default settings of a 'Ball' object.
    self.shape("circle")
    self.color("white")
    self.penup()

    # Initial velocity.
    self.xMove = 5
    self.yMove = 5

    # Frame refresh rate (144 FPS).
    self.sleep = 0.0144

  # Keeps the ball in movement.
  def movement(self):
    newX = self.xcor() + self.xMove
    newY = self.ycor() + self.yMove
    self.goto(newX, newY)

  # Lets the ball bounce in different directions.
  def bounce_y(self):
    self.yMove *= -1
  
  def bounce_x(self):
    if self.xMove > 0 and self.xMove != 25:
      self.xMove += 0.5
      self.yMove += 0.5

    elif self.xMove < 0 and self.xMove != -25:
      self.xMove += -0.5
      self.yMove += -0.5

    self.xMove *= -1

  # Resets the ball's position and velocity upon a player scoring.
  def reset_position(self):
    self.goto(0, 0)

    # Sets the ball to either direction based on which side of the arena it was scored.
    if self.xMove < 0:
      self.xMove = 5
      self.yMove = 5

    else:
      self.xMove = -5
      self.yMove = -5

  # Resets the object to its defaults.
  def reset_ball(self):
    self.goto(0, 0)
    self.xMove = 5
    self.yMove = 5