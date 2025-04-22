import time
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
BORDER_LIMIT = 290
game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    score = 0
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.writeScore()

    if snake.head.xcor() > BORDER_LIMIT or snake.head.xcor() < -BORDER_LIMIT or snake.head.ycor() > BORDER_LIMIT or snake.head.ycor() < -BORDER_LIMIT:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()