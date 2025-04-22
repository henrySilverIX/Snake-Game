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


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True


while game_is_on:
    score = 0
    screen.update()
    time.sleep(0.1)


    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.writeScore()



screen.exitonclick()