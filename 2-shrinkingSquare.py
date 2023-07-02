import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Turtle Python")


turtle_instance = turtle.Turtle()
turtle_instance.color("red")

def shrinkinSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

shrinkinSquare(100)
shrinkinSquare(80)
shrinkinSquare(60)
shrinkinSquare(40)
turtle.done()

