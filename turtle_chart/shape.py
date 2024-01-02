from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape('turtle')


def rand_color_x():
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    tim.pencolor(r, g, b)


for shape in range(3, 11):
    rand_color_x()
    for side in range(shape):
        tim.fd(100)
        tim.right(360/shape)

screen.exitonclick()
