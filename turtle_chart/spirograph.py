from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape('turtle')
tim.speed('fastest')


def rand_color_x():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim.pencolor(r, g, b)


def draw_spiro(size):
    for step in range(int(360 / size)):
        rand_color_x()
        tim.circle(100)
        tim.setheading(tim.heading() + size)


draw_spiro(1)

screen.exitonclick()
