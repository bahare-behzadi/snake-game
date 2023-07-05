from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score_board
screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("3.png")
screen.title("snake game 🐍")
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
score_board = Score_board()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # eating food
    if snake.snake_head.distance(food) < 15:
        food.create_new_food()
        score_board.increase_score()
        snake.extend()
    # collision with walls
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        score_board.game_over()
        game_is_on = False

    # collision with itself
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()
screen.exitonclick()
