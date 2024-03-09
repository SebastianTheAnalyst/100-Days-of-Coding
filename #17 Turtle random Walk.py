# Turtle random Walk

from turtle import Turtle, Screen
import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for _ in range(200):
    timmy.color(random_color())
    angle = random.choice([90, 180, 0, 270])
    direction = random.choice([timmy.left, timmy.right])
    direction(angle)
    timmy.width(5)
    timmy.speed(50)
    timmy.forward(25)

screen = Screen()
screen.exitonclick()


