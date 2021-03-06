from shutil import move
import time
from turtle import Screen
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Player
player = Player("black")

#SCoreboard
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(player.move_up, "Up")


car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    #detect sucessful crossing

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()

    
