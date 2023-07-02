import turtle
import time



myScreen = turtle.Screen()
myScreen.title("OYUNUM")
myScreen.bgcolor("gray")


wn = turtle.Screen()

skor_basligi = turtle.Turtle()
skor_basligi.color("blue")
skor_basligi.penup()

skor_degeri = turtle.Turtle()
skor_degeri.color("green")
skor_degeri.penup()

time_basligi = turtle.Turtle()
time_basligi.color("blue")
time_basligi.penup()

time_degeri = turtle.Turtle()
time_degeri.color("green")
time_degeri.penup()

tosbaa = turtle.Turtle()
time_degeri.color("black")
time_degeri.penup()



def sayac():
    time_off = 3
    time_degeri.setposition(50, 300)
    while True:
        time_degeri.hideturtle()
        time_degeri.reset()
        time_degeri.write(time_off)
        time.sleep(1)
        time_off -= 1

        if time_off == 0:
            time_degeri.reset()
            time_degeri.write("Zaman Bitti", move=False, align='center', font=("arial", 20, "normal"))
            break

skor = 0
def skor_arttir():
    skor = 1
    return print(skor)

sayac()
skor_basligi.setposition(0, 350)
skor_basligi.hideturtle()
skor_basligi.write(arg='Score:', move=True, align='center', font=("arial", 20, "normal"))

skor_degeri.setposition(50, 350)
skor_degeri.hideturtle()
skor_degeri.write(skor, move=True, align='center', font=("arial", 20, "normal"))

time_basligi.setposition(0, 300)
time_basligi.hideturtle()
time_basligi.write(arg='Time: ', move=True, align='center', font=("arial", 20, "normal"))

tosbaa.setposition(50, 50)
tosbaa.onclick(skor_arttir)




wn.mainloop()
