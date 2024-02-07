import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title('My Frogger Game')

player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.onkey(player.go_up, key='w')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.car_move()

    if player.ycor() > 280:
        # increase level by getting to end
        scoreboard.level_up()
        player.level_up()
        car.level_up()

    # player collision with car
    for x in car.all_cars:
        if x.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
