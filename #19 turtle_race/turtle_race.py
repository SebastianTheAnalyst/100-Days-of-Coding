from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make Yur bet", "Which turtle will win. Enter a color")
colors = ["red",  "yellow","blue", "green","orange",  "purple"]
position = [-150, -90, -30, 30, 90, 150]
all_turtles = []


for turtle_index in range(0, 6):
    racer = Turtle(shape="turtle")
    racer.color(colors[turtle_index])
    racer.penup()
    racer.goto(-230, position[turtle_index])
    all_turtles.append(racer)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the Winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the Winner")


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()










