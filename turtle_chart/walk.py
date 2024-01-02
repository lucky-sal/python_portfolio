from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape('turtle')
tim.speed('fastest')
tim.pensize(15)
directions = [0, 90, 180, 270]


def rand_move():
    tim.setheading(random.choice(directions))


def rand_color_x():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim.pencolor(r, g, b)


for step in range(200):
    rand_color_x()
    rand_move()
    tim.fd(30)

screen.exitonclick()
