import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.bgcolor("white")
screen.title("Turtle Crossing Game")
timmy = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(timmy.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    #DETECT TURTLE'S COLLISION WITH THE CAR
    for car in cars.all_cars:
        if car.distance(timmy) < 20:
            game_is_on = False
            scoreboard.game_over()

    #DETECT IF TURTLE REACHED FINISH LINE # if timmy.ycor() > 280:
    if timmy.is_finish_line_reached():
        timmy.reset_position()
        scoreboard.increase_level()
        cars.increase_car_speed()

screen.exitonclick()