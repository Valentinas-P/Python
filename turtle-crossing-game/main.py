import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from gameover import GameOver

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("turtle-crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard(-280, 260)
gameover = GameOver()

screen.listen()
screen.onkey(player.move_player, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_car()
    car_manager.create_a_car()

    for car in car_manager.car_fragment:
        if car.distance(player) < 30:
            gameover.game_over()
            game_is_on = False

    if player.ycor() > 290:
        print("player reached")
        scoreboard.increase_score()
        player.refresh_player()
        car_manager.level_up()


screen.exitonclick()
