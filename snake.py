import keyboard
from turtle import *
import time





snake = Turtle()
snake.shape('square')
snake.color('green')
snake.up()

def checkdirection(direction, snake):
    match (direction):
        case("right"):
            direction = "left"
            return snake.left(90)
        case("left"):
            direction = "right"
            return snake.right(90)
            
    
def move(key, snake):
    direction = "right"
    snake.speed(0)
    match (key):
        case("w"):
            checkdirection(direction, snake)
            return snake.forward(50)
        case("d"):
            checkdirection(direction, snake)
            return snake.forward(50)
        case("s"):
            checkdirection(direction, snake)
        case("a"):
            checkdirection(direction, snake)
            return snake.forward(50)
        case default:
            return snake.forward(50)



while True != False:
    key = keyboard.read_key()
    move(key, snake)
    time.sleep(1)
    
