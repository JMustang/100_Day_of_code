from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backward():
	tim.backward(10)

def turn_left():
	tim.left(90)

def turn_right():
	tim.right(90)

def clear():
	tim.clear()
	tim.penup()
	tim.home()
	tim.pendown()

screen.listen()
screen.onkey(key="d", fun=move_forwards)
screen.onkey(key="a", fun=move_backward)
screen.onkey(key="w", fun=turn_left)
screen.onkey(key="s", fun=turn_right)

screen.onkey(key="c", fun=clear)
screen.exitonclick()
