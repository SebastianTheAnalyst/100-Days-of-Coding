from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
# Bind keys for right paddle
screen.onkeypress(r_paddle.move_up, "o")
screen.onkeypress(r_paddle.move_down, "k")

# Bind keys for left paddle
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()
    #Detect if r_paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if l_paddle misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    #Detect collision with the paddle
    if ball.xcor() >320 and ball.distance(r_paddle) < 50 or ball.xcor() <-320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()


screen.exitonclick()