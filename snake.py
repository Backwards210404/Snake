import keyboard
from turtle import *
import time


snake = Turtle()
snake.shape('square')
snake.color('green')
snake.up()           

def move(key, snake, direction):
    
    snake.speed(0)
    match (key):
        case("w"):
            if (direction == "right"):
                snake.left(90)
            elif (direction == "left"):
                snake.right(90)
            snake.forward(50)
            direction = "up"
            return direction
        case("d"):
            if (direction == "up"):
                snake.right(90)
            elif (direction == "down"):
                snake.left(90)
            snake.forward(50)
            direction = "right"
            return direction
        case("s"):
            if (direction == "right"):
                snake.right(90)
            elif (direction == "left"):
                snake.left(90)
            snake.forward(50)
            direction = "down"
            return direction
        case("a"):
            if (direction == "up"):
                snake.left(90)
            elif (direction == "down"):
                snake.right(90)
            snake.forward(50)
            direction = "left"
            return direction
        case default:
            snake.forward(50)



direction = "right" 
while True != False:
    key = keyboard.read_key()
    direction = move(key, snake, direction)
    time.sleep(1)
