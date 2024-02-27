from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

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

    # Detect collision with food.
    if snake.fragments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.fragments[0].xcor() > 280 or snake.fragments[0].xcor() < -280 or snake.fragments[0].ycor() > 280 or \
            snake.fragments[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for fragment in snake.fragments[1:]:
        if snake.fragments[0].distance(fragment) < 10:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()
