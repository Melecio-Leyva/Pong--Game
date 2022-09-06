#import all classes necessary
import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
#create class object for the game.
ball = Ball()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
scoreboard = Scoreboard()
screen.listen()
# Up down for both paddles. and thier functions
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True
#keep game going with true.
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        # bounce the ball
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # right middle misses scored point and reset ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # if left paddle misses scored point and reset ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        
screen.exitonclick()
