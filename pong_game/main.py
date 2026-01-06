from turtle import Screen, Turtle
import time
from sliders import Sliders
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

user1 = Sliders(350, 0)
user2 = Sliders(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(user1.move_up, "Up")
screen.onkey(user1.move_down, "Down")
screen.onkey(user2.move_up, "w")
screen.onkey(user2.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.sleep_time)
    screen.update()
    ball.move()
    if ball.check_bounce():
        ball.bounce_y()
    if ball.distance(user1) < 50 and ball.xcor() > 320 or ball.distance(user2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()
    
    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()



