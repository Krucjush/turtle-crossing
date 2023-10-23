from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def generate_car(self, difficulty_list):
        random_chance = random.randint(1, 6)
        if random_chance in difficulty_list:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            car.setheading(180)
            self.cars.append(car)

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT
