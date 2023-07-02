import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("turtle")


turtle_instance = turtle.Turtle()
turtle_instance.color("red")

turtle_colors = ["red","gray","yellow","blue","pink","green","orange"]

for i in range(6):
    turtle_instance.color(turtle_colors[i %  6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)

# turtle.done() = turtle.mainloop()
turtle.mainloop()