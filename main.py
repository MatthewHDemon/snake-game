from turtle import Turtle, Screen
import time

from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# board game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Game")
#disable default Turtle animation
screen.tracer(0)



#Creo a la serpiente - Instanciar el objeto serpiente
my_snake = Snake()

#Creamos el objeto comida
food = Food()

#Creamos el objeto tablero
scoreboard = ScoreBoard()

#snake animation
game_is_on = True

screen.listen()
screen.onkey(my_snake.up, "w") #no se le pone parentesis, sino no tomaría en cuenta la tecla y se ejecutaría automaticamente
screen.onkey(my_snake.down, "s")
screen.onkey(my_snake.left, "a")
screen.onkey(my_snake.right, "d")


while game_is_on:
    screen.update()
    time.sleep(0.5)

    my_snake.move()

    #Detecta colisión de comida
    if my_snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        my_snake.extend()

    #Detector de colisiones de paredes
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
       """ game_is_on = False
       scoreboard.game_over() """

    #Detector de colisiones de segmentos de serpiente
    for segment in my_snake.segments:
        """ if segment == my_snake.head:
            pass
        elif my_snake.head.distance(segment) < 10: """ #Utilizar slicers para descartar linea 56 y 57
            game_is_on = False
            ScoreBoard.game_over()

    


screen.exitonclick()