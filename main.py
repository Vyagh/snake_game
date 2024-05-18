from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Famous Snake Game")
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

    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with Food.
    #  We will use .distance() to measure distance with another turtle instance(Food)
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # Detect Collision with Wall.
    #  Screen does not clear because we do not clear it here
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Detect Collision with Tail.
    # ------
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:  # Ends game immediately because first segment is head itself so add a
    #         game_is_on = False                      # if above
    #         scoreboard.game_over()
    # ------

    # Because the above section is very wordy(Just for detecting snake head not colliding with its tail we write alot)
    #  So we would implement slicing

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()


#                                                Project Flow
# We can delete the Classes or modules grayed out in the very start cz they are not being used.
#


