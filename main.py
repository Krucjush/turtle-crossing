import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from difficulty import Difficulty

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
difficulty = Difficulty()

screen.listen()
screen.onkey(player.move, "Up")
if not difficulty.difficulty_set:
    screen.onkey(difficulty.easy_difficulty, "1")
    screen.onkey(difficulty.medium_difficulty, "2")
    screen.onkey(difficulty.hard_difficulty, "3")
    screen.onkey(difficulty.manic_difficulty, "4")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    car_manager.generate_car(difficulty.difficulty)
    if player.ycor() == player.finish_line:
        player.reset_position()
        car_manager.speed_up()
        scoreboard.update_score()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
