# from turtle import Turtle, Screen

# tim = Turtle()

# tim.shape("turtle")
# tim.color("green")

# def drawdot(space, x):
#   for i in range (x):
#     for j in range(x):
#       tim.dot()
#       tim.forward(space)
#     tim.backward(space * x)
#     tim.right(90)
#     tim.forward(space)
#     tim.left(90)

# tim.penup()
# drawdot(100, 5)
# tim.hideturtle()

import turtle as t

tim = t.Turtle()

for _ in range(15):
  tim.forward(10)
  tim.penup()
  tim.forward(10)
  tim.pendown()