import turtle
'''
drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")

turtle_instance_1 = turtle.Turtle()
turtle_instance_1.forward(200)

turtle_instance_2 = turtle.Turtle()
turtle_instance_2.left(45)
turtle_instance_2.forward(100)

turtle.done()
'''



'''
kare = turtle.Screen()
kare.bgcolor("red")
kare.title("KARE")

kare_tosba = turtle.Turtle()

for i in range(4):
    kare_tosba.forward(100)
    kare_tosba.left(90)
turtle.done()
'''

'''
yildiz = turtle.Screen()
yildiz.bgcolor("gray")
yildiz.title("YILDIZ")
yildiz_ciz = turtle.Turtle()
for i in range(5):
    yildiz_ciz.left(144)
    yildiz_ciz.forward(200)
turtle.done()
'''


# İŞİ BİRAZ DİNAMİKLEŞTİRELİM
dinamik = turtle.Screen()
dinamik.bgcolor("gray")
dinamik.title("dinamik")

dinamik_cizim = turtle.Turtle()

kenar_sayisi = 7
donus_acisi = 360/kenar_sayisi
cizgi_uzunlugu = 150
for i in range(kenar_sayisi):
    dinamik_cizim.left(donus_acisi)
    dinamik_cizim.forward(cizgi_uzunlugu)
turtle.done()
