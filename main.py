# ATTENTION: The entire game - from start to end - will ONLY be displayed in the 'Output' tab. Please, keep it open at all times.

# Author: Murad Dashdamirov
# Date: May 21st, 2024
# Name: Pong
# Purpose: to entertain the user in the classic game of pong.

# Imports the necessary python packages for graphics and frame refreshing.
from turtle import Screen, Turtle
import time

# Imports classes from adjacent files.
from Classes.paddles import Paddle
from Classes.ball import Ball
from Classes.scoreboard import Scoreboard
from Classes.controls import Key
from Classes.arena import Setup

# Screen setup.
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1024, height=700)
screen.title("Pong")

timesPlayed = 0

# Disables animations.
screen.tracer(0)

# Sets up a text writing object.
text = Turtle()
text.hideturtle()
text.pencolor("white")
text.penup()

# Title screen.
text.goto(-400, 0)
text.write("Pong!", font=("Georgia", 100, "bold", "italic"))
text.goto(0, -100)
text.write("by Murad D.", font=("Futura", 50))
text.goto(0, -260)
text.write("_", align="center", font=("Futura", 20, "bold"))
text.goto(0, -320)
text.write("Press 's' to start | Press 'i' for instructions | Press 'l' to leave", align="center", font=("Futura", 20, "bold"))

# ------------------------------------ Functions ------------------------------------ #

def run():
  global timesPlayed
  global gameIsOn
  global playerOne
  global playerTwo
  global ball
  global scoreboard
  global velocityIndicator
  
  # Disables event listener for 'instructions' and 'farewell' functions.
  screen.onkey(None, 'i')
  screen.onkey(None, 'l')

  timesPlayed += 1
  
  # Clears the text that the turtle had written.
  text.clear()
  text.hideturtle()

  # Displays additional information.
  text.goto(-500, 320)
  text.write("P1", align="left", font=("Cascadia", 10, "bold"))
  text.goto(500, 320)
  text.write("P2", align="right", font=("Cascadia", 10, "bold"))
  text.goto(500, -340)
  text.write("press 'r' to reset | 'p' to pause | 'l' to leave", align="right", font=("Futura", 10, "bold"))

  # Sets up the arena ONCE.
  if timesPlayed == 1:
    # Enables animations.
    screen.tracer(1)
    
    # Sets up the turtle that will 'draw' the arena.
    line = Setup(heading=270, position=(0, 370))
    circle = Setup(heading=0, position=(0, -10))

    # Arena setup.
    line.draw_line()
    circle.draw_circle(radius=10)
    
    # Interactive objects.
    playerOne = Paddle((-462, 0))
    playerTwo = Paddle((462, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    # Indicator setup.
    velocityIndicator = Turtle()
    velocityIndicator.hideturtle()
    velocityIndicator.pencolor("white")
    velocityIndicator.penup()

    # Disables animations
    screen.tracer(0)

  # Sets up controls.
  wKey = Key('w')
  sKey = Key('s')
  upKey = Key('Up')
  downKey = Key('Down')

  # Activates event listeners for 'reset' and 'pause' functions.
  screen.onkey(reset, 'r')
  screen.onkey(pause, 'p')

  # Starts the game.
  gameIsOn = True
  
  while gameIsOn:
    # Sets up input(s).
    lKey = Key("l")
    
    # Frame refresher.
    time.sleep(ball.sleep)
    screen.update()
    ball.movement()

    # Runs the following if the ball has reached its maximum speed.
    if ball.xMove == 25 or ball.xMove == -25:
      velocityIndicator.clear()
      velocityIndicator.hideturtle()
      velocityIndicator.goto(-500, 300)
      velocityIndicator.write("MAX. BALL VELOCITY REACHED!", align="left", font=("Cascadia", 10, "italic"))

    else:
      velocityIndicator.clear()
      velocityIndicator.hideturtle()

    # Paddle event listeners.
    if wKey.down and sKey.down == False and upKey.down == False and downKey.down == False:
      playerOne.up()

    if sKey.down and wKey.down == False and upKey.down == False and downKey.down == False:
      playerOne.down()

    if upKey.down and sKey.down == False and wKey.down == False and downKey.down == False:
      playerTwo.up()

    if downKey.down and sKey.down == False and upKey.down == False and wKey.down == False:
      playerTwo.down()

    # Makes it possible for multiple event listeners to execute simultaneously.
    if wKey.down and upKey.down:
      playerOne.up()
      playerTwo.up()

    if sKey.down and downKey.down:
      playerOne.down()
      playerTwo.down()

    if sKey.down and upKey.down:
      playerOne.down()
      playerTwo.up()

    if wKey.down and downKey.down:
      playerOne.up()
      playerTwo.down()

    # Runs the following lines of code if the ball touches the top and bottom boundaries.
    if ball.ycor() > 320 or ball.ycor() < -320:
      ball.bounce_y()
    
    # Runs the following lines of code if the ball touches one of the two paddles.
    if ball.distance(playerOne) < 60 and ball.xcor() < -432 and ball.xcor() > -462 and ball.xMove < 0:
      ball.bounce_x()
      
    if ball.distance(playerTwo) < 60 and ball.xcor() > 432 and ball.xcor() < 462 and ball.xMove > 0:
      ball.bounce_x()

    elif ball.distance(playerOne) < 60 and ball.xcor() < -432 and ball.xMove < 0:
      ball.bounce_y()

    elif ball.distance(playerTwo) < 60 and ball.xcor() > 432 and ball.xMove > 0:
      ball.bounce_y()

    # Runs the following lines of code if the ball is out of bounds (beyond the left and right boundaries).
    if ball.xcor() > 512:
      scoreboard.p1_update()
      scoreboard.update_scoreboard()
      ball.reset_position()

    if ball.xcor() < -512:
      scoreboard.p2_update()
      scoreboard.update_scoreboard()
      ball.reset_position()

    # Checks if one of the players has already scored seven points.
    if scoreboard.p1Score == 7 or scoreboard.p2Score == 7:
      gameIsOn = False
      results(scoreboard.p1Score, scoreboard.p2Score)

    # Exits the game if the user chose to leave.
    if lKey.down:
      gameIsOn = False
      farewell()

def instructions():
  # Clears the text that the turtle had written.
  text.clear()
  text.hideturtle()

  # Displays instructions.
  text.goto(0, 280)
  text.write("Instructions", align="center", font=("Georgia", 50, "bold"))
  text.goto(-500, 250)
  text.write("Controls:", align="left", font=("Futura", 25, "bold"))
  text.goto(-470, 200)
  text.write("Player 1: 'W' to ascend, 'S' to descend", align="left", font=("Futura", 25))
  text.goto(-470, 150)
  text.write("Player 2: '↑' to ascend, '↓' to descend", align="left", font=("Futura", 25))
  text.goto(-500, 100)
  text.write("Goal:", align="left", font=("Futura", 25, "bold"))
  text.goto(-470, 50)
  text.write("First to accumulate 7 points wins!", align="left", font=("Futura", 25))
  text.goto(-500, 0)
  text.write("How does the game work?:", align="left", font=("Futura", 25, "bold"))
  text.goto(-470, -50)
  text.write("1. There is one paddle for each player.", align="left", font=("Futura", 25))
  text.goto(-470, -100)
  text.write("2. There is a ball. You have to outplay your opponent", align="left", font=("Futura", 25))
  text.goto(-470, -150)
  text.write("    by trying to get the ball just past their paddle to score.", align="left", font=("Futura", 25))
  text.goto(-470, -200)
  text.write("3. The ball accelerates with each bounce off the paddles.", align="left", font=("Futura", 25))
  text.goto(0, -260)
  text.write("_", align="center", font=("Futura", 20, "bold"))
  text.goto(0, -320)
  text.write("Press 's' to start | Press 'l' to leave", align="center", font=("Futura", 20, "bold"))

def farewell():
  # Resets the screen's properties.
  screen.clear()
  screen.bgcolor("black")

  # Disables animations.
  screen.tracer(0)

  # Clears the text that the turtle had written.
  text.clear()
  text.hideturtle()

  # Displays different farewell screens depending if the user has played the game or have not.
  if timesPlayed > 0:
    text.goto(0, 0)
    text.write("Thank you for playing.", align="center", font=("Georgia", 50, "bold"))

  else:
    text.goto(0, 80)
    text.write("You always have the time", align="center", font=("Georgia", 50, "bold"))
    text.goto(0, 0)
    text.write("to change your mind.", align="center", font=("Georgia", 50, "bold"))
    text.goto(0, -80)
    text.write("See you later!", align="center", font=("Georgia", 50, "italic", "bold"))

def pause():
  global gameIsOn

  # Pauses/unpauses the game depending on whether it has been already paused or not.
  if gameIsOn:
    gameIsOn = False
    text.goto(-500, -340)
    text.write("*paused", align="left", font=("Futura", 10, "italic"))
    
  else:
    gameIsOn = True
    text.clear()
    run()

def reset():
  playerOne.reset_paddle((-462, 0))
  playerTwo.reset_paddle((462, 0))
  ball.reset_ball()
  scoreboard.reset_scoreboard()

def restart():
  global timesPlayed

  # Resets the essential variables and reruns the game.
  timesPlayed = 0
  scoreboard.p1Score = 0
  scoreboard.p2Score = 0
  run()

def results(p1Score, p2Score):
  # Resets the screen's properties.
  screen.clear()
  screen.bgcolor("black")

  # Disables animations.
  screen.tracer(0)
  
  text.goto(0, 0)
  
  # Displays different result screens depending which player won.
  if p1Score == 7:
    text.write("Player 1 wins!", align="center", font=("Georgia", 50, "bold"))
    text.goto(0, -260)
    text.write("_", align="center", font=("Futura", 20, "bold"))
    text.goto(0, -320)
    text.write("Press 'r' to restart | Press 'l' to leave", align="center", font=("Futura", 20, "bold"))

  if p2Score == 7:
    text.write("Player 2 wins!", align="center", font=("Georgia", 50, "bold"))
    text.goto(0, -260)
    text.write("_", align="center", font=("Futura", 20, "bold"))
    text.goto(0, -320)
    text.write("Press 'r' to restart | Press 'l' to leave", align="center", font=("Futura", 20, "bold"))

  # Event listeners.
  screen.onkey(restart, 'r')
  screen.onkey(farewell, 'l')

# ----------------------------------------------------------------------------------- #

# Event listeners.
screen.onkey(run, 's')
screen.onkey(instructions, 'i')
screen.onkey(farewell, 'l')

# Activates event listeners.
screen.listen()

# Keeps the screen displayed.
screen.mainloop()