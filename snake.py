import turtle
window = turtle.Screen()
window.bgcolor('dark salmon')
window.tracer(0)

Snake = turtle.Turtle()
Snake.shape('square')
Snake.color('green')
Snake.penup()           
global direction
direction = "right"
def up():
    Snake.sety(Snake.ycor())
    global direction
    direction = "up"

def down():
    Snake.sety(Snake.ycor())
    global direction
    direction = "down"

def left():
    Snake.forward(-0.01)
    global direction
    direction = "left"

def right():
    Snake.forward(0.01)
    global direction
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
print(window.listen())

while True:
  move(direction)
  window.update()
