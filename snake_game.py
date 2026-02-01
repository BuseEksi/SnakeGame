import time
from turtle import Screen,Turtle

from food import Food
from scoreboard import Scoreboard
from create_snake import Snake

MIN_LENGTH_TO_COLLIDE =4
FONT = ('Courier', 20, 'normal')



screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake game")

snake=Snake()
food=Food()
game_over=Turtle()
game_over.penup()
game_over.goto(0, 0)
game_over.hideturtle()
scoreboard=Scoreboard()



screen.listen()


screen.onkey(snake.turn_up, "w")
screen.onkey(snake.turn_down, "s")
screen.onkey(snake.turn_left, "a")
screen.onkey(snake.turn_right, "d")

screen.onkey(snake.turn_up, "W")
screen.onkey(snake.turn_down, "S")
screen.onkey(snake.turn_left, "A")
screen.onkey(snake.turn_right, "D")

screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.new_location()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset_score()
        snake.reset()
        game_over.color("white")
        game_over.write("GAME OVER", align="center", font=FONT)

        game_is_on = False


    if len(snake.segment_list) > MIN_LENGTH_TO_COLLIDE:
        for segment in snake.segment_list[1:]:
            if snake.head.position() == segment.position():
                scoreboard.reset_score()
                snake.reset()
                game_over.color("white")
                game_over.write("GAME OVER", align="center", font=FONT)
                game_is_on = False












screen.exitonclick()