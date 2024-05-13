import turtle
window = turtle.Screen()
window.bgcolor('orange')
window.tracer(0)

Snake = turtle.Turtle("square")
Snake.color('green')
Snake.penup()   
global direction
direction = "right"

def createfood():
    food = turtle.Turtle("round")
    food.color('red')
    food.penup()
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
            Snake.forward(0.01)
        case("up"):
            Snake.sety(Snake.ycor()+0.01)
        case("down"):
            Snake.sety(Snake.ycor()-0.01)
        case("left"):
            Snake.forward(-0.01)

window.onkeypress(up, "Up")
window.onkeypress(down, "Down")
window.onkeypress(right, "Right")
window.onkeypress(left, "Left")
window.onkeypress(up, "w")
window.onkeypress(down, "s")
window.onkeypress(right, "d")
window.onkeypress(left, "a")
print(window.listen())

while True:
  createfood()
  move(direction)
  window.update()
  
