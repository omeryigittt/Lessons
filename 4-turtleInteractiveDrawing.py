import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("DENEME")


turtle_ins = turtle.Turtle()

def turtle_forward():
    turtle_ins.forward(100)

def rotateAngelRight():
    # bunu da kullanabiliriz yönlendirmek için
    turtle_ins.setheading(turtle_ins.heading()-10)
    #turtle_ins.right(10)

def rotateAngelLeft():
    turtle_ins.setheading(turtle_ins.heading()+10)
    #turtle_ins.left(10)

def clear_screen():
    turtle_ins.clear()

def turtle_return_home():
    turtle_ins.penup()
    turtle_ins.home()
    turtle_ins.pendown()

def turtle_pen_up(): # kalemi kağıttan ayırır
    turtle_ins.penup()

def turtle_pen_down(): # kalemi kağıda değdirir
    turtle_ins.pendown()



drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=rotateAngelRight,key="Down")
drawing_board.onkey(fun=rotateAngelLeft,key="Up")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=turtle_return_home,key="h")
drawing_board.onkey(fun=turtle_pen_up,key="u")
drawing_board.onkey(fun=turtle_pen_down,key="d")


drawing_board.mainloop()