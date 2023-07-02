import turtle
import random

screen = turtle.Screen()
screen.bgcolor("gray")
screen.title("YAKALA")
FONT = ("Arial", 20, "normal")
score = 0
game_over = False

# turtle list
turtle_list = []

#countdown
countdown_turtle = turtle.Turtle()

# score turtle
score_turtle = turtle.Turtle()
def setup_score_turtle():
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.setpos(0, y)
    score_turtle.color("dark blue")
    score_turtle.write(arg=f"Score: 0", move=False, align="center", font=FONT)


grid_size = 10


def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        # print(x,y)
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)


x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]


def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    hide_turtles()
    if not game_over:
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,500)
        # recursive funk: yani kendi içinde kendini tekrar çağıran fonksiyon
        # normalde ontimer bir kere çalışır
        # ama biz her defasında kendisini çağırdığımızdan aslında
        # o kadar milisaniyede bir çalıştırmış oluruz


def countdown(time):
    global game_over
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.setpos(0, y-30)
    countdown_turtle.color("dark blue")
    countdown_turtle.write(arg=f"Score: 0", move=False, align="center", font=FONT)
    if time > 0:
        countdown_turtle.hideturtle()
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time-1),1000)
    else:
        game_over = True
        countdown_turtle.hideturtle()
        countdown_turtle.clear()
        countdown_turtle.write(arg="Game Over", move=False, align="center", font=FONT)


turtle.tracer(0)  # tracer 0 ile 1 arasına yazılanların animasyonları beklenmez
setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
countdown(10)
turtle.tracer(1)  # tracer 0 ile 1 arasına yazılanların animasyonları beklenmez

turtle.mainloop()
# mainloop metodu milisaniylerle sürekli projeyi tarar ve seknkron işlemleri
# aynı anda çalışmasına olanak sağlar.
# dolayısı ile kodların sırasıyla işletilmesinden bağımsız olarak
# senkron çalışma imkanı olan metodları senkron çalıştırabiliriz.
# bunun yanında mainloop() metodu olsa bile senkron çalışmayan fonklarda var
# örneğin time.sleep(2) 2 saniye bekle sonra aşağıdaki koda in demek
# dolyısı ile o bitmeden diğerini çalıştıramayacağından mainloop olması da
# yeterli değil.