from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 9)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(300, random.randint(-200, 240))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT








