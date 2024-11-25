#Blayne Hoy
#U3 Project
"""
IMPORTANT
To run your code in this project,
open the Terminal and enter the following:

python main.py    then enter

Your output will be visualized in the 
Virtual Desktop
"""
import turtle
import random


branches = 7
turn_angle = 10
shrink_factor = 0.8
t = turtle.Turtle()

def tree(size, depth):
  if depth >= 1:
    if random.random() > 0.33:
      t.width(depth)
      t.color(colors(depth))
      t.forward(size)
      t.right(turn_angle)
      tree(size*shrink_factor, depth-1)
      t.right(turn_angle)
      tree(size*shrink_factor, depth-1)
      t.left(3*turn_angle)
      tree(size*shrink_factor, depth-1)
      t.left(turn_angle)
      tree(size*shrink_factor, depth-1)
      t.right(2*turn_angle)
      t.color(colors(depth))
      t.backward(size)



def colors(depth):
  if branches - depth < 5:
    return 'white'
  else:
    return 'purple'


if __name__ == "__main__":
  random.seed(46)
  t.speed(0)
  turtle.bgcolor('black')
  t.setheading(90)
  turtle.colormode(255)
  tree(40, branches)
  turtle.done()
