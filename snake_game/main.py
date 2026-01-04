from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(n=0, delay=0)

snake = Snake()
food = Food()

score = 0

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score += 1
        snake.extend()

    if snake.hit_wall():
        game_is_on = False
        print("Game Over")
        print(f"Score: {score}")

screen.title("My Snake Game")
screen.exitonclick()
