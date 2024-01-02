from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.hideturtle()
tim.speed('fastest')
tim.teleport(-250, -250)

color_list = [(189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 186, 214), (208, 225, 208),
              (211, 209, 210), (64, 43, 43), (171, 183, 170)]


def dot_color():
    tim.dot(20, random.choice(color_list))


def left_turn():
    dot_color()
    tim.left(90)
    tim.penup()
    tim.fd(50)
    tim.left(90)
    tim.pendown()


def right_turn():
    dot_color()
    tim.right(90)
    tim.penup()
    tim.fd(50)
    tim.right(90)
    tim.pendown()


def stamp(num_stamps):
    for steps in range(num_stamps):
        dot_color()
        tim.penup()
        tim.fd(50)
        tim.pendown()


for lines in range(5):
    stamp(10)
    left_turn()
    stamp(10)
    right_turn()

screen.exitonclick()
