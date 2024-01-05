import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=550, height=450)

is_race_on = False
colors = ['blue', 'red', 'green', 'purple', 'yellow', 'orange']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.setpos(x=-250, y=y_positions[turtle_index])
    all_turtles.append(tim)


user_guess = turtle.textinput(title='Make your bet:', prompt='Which turtle will win the race? Enter a color').lower()

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_guess:
                print(f'You won! the {winner} turtle won the race!')
            else:
                print(f'Sorry you bet wrong, {winner} won the race!')

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
