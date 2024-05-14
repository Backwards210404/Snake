import turtle
from random import *
window = turtle.Screen()
window.bgcolor('orange')
window.tracer(0)

Snake = turtle.Turtle("square")
Snake.color('green')
Snake.penup()
   
global direction
direction = "right"

def createfood():
    global food
    food = turtle.Turtle("circle")
    food.color('red')
    food.penup()
    return food
def up():
    global direction
    if direction != "down":
        Snake.sety(Snake.ycor())
        direction = "up"

def down():
    global direction
    if direction != "up":
        Snake.sety(Snake.ycor())
        direction = "down"

def left():
    global direction
    if direction != "right":
        Snake.forward(-0.01)
        direction = "left"

def right():
    global direction
    if direction != "left":
        Snake.forward(+0.01)
        direction = "right"
        
def move(direction):
    match (direction):
        case ("right"):
            Snake.forward(0.1)
        case("up"):
            Snake.sety(Snake.ycor()+0.1)
        case("down"):
            Snake.sety(Snake.ycor()-0.1)
        case("left"):
            Snake.forward(-0.1)

window.onkeypress(up, "Up")
window.onkeypress(down, "Down")
window.onkeypress(right, "Right")
window.onkeypress(left, "Left")
window.onkeypress(up, "w")
window.onkeypress(down, "s")
window.onkeypress(right, "d")
window.onkeypress(left, "a")
print(window.listen())
food = createfood()
def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10


while True:
    move(direction)
    if is_collided_with(Snake, food):
        food.goto(randint(0,200),randint(0,200))
        
        
    window.update()
  
  
