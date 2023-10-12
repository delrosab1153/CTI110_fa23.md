"""
CTI-110-0004
P4LAB1 - Turtle shapes in loops
delrosab1153
Thu 10/12/2023
"""

import random
import turtle

t = turtle.Turtle()
t.pensize(2)

# Set screensize
screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("P4LAB1 - Turtle shapes in loops")

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Set variables
REPEAT = 5
for time in range(REPEAT):
  X = random.randrange(-200, 200)
  Y = random.randrange(-200,200)
  t.penup()
  t.goto(X, Y)
  t.pendown()
  PEN_COLOR = random.choice(COLORS)
  SIDES = random.randrange(3, 12)
  LENGTH = random.randrange(10, 100)
  ANGLE = 360 / SIDES
  FILL = True
  FILL_COLOR = random.choice(COLORS)
  
  if FILL == True:
    t.begin_fill()
    t.fillcolor(FILL_COLOR)
    
  # Draw a shape
  t.pencolor(PEN_COLOR)
  for _side in range(SIDES):
    # Draw a star (sort of)
    '''
    for star_side in range(3):
      t.right(120)
      t.forward(LENGTH)'''
  
    # Draw the sides of the shape
    t.forward(LENGTH)
    t.right(ANGLE)
  
  if FILL == True:
    t.end_fill()
    
# Keep window open at end
turtle.done()