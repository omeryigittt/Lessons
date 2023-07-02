import tkinter

window = tkinter.Tk()

# window pencere
window.title("Tkinter Denemesi")
window.minsize(height=300,width=450)


# label
my_label=tkinter.Label(text="This is a label", font=("Arial",20,"italic"))
# parametreleri yukarda parantezde iken de yazabiliriz.
# sonrasında aşağıdaki gibi config deyip de ekleyebiliriz.
my_label.config(bg="black",fg="white")
# konumlandırma fonksiyonlarından biri (Ortalı ve ögeler alt alta)
#my_label.pack()
#diğer konumlandırma direk kordinat verme ile
#my_label.place(x=50,y=50)
#diğer konumlandırma grid sistemi
my_label.grid(row=0,column=0)

def click_button():
    user_input = my_entry.get()
    print(user_input)

# button
# fonksiyon çağrılacaksa sadece bu duruma özel üst satırlarda önceden fonksiyonun tanımlı olması gerekir. Altındaki fonksiyonu göremiyor.
my_button = tkinter.Button(text="Button",command=click_button)
#my_button.pack()
#my_button.place(x=150,y=150)
my_button.grid(row=1,column=1)


# entry
my_entry = tkinter.Entry(width=50)
#my_entry.pack()
#my_entry.place(x=250,y=250)
my_entry.grid(row=0,column=3)









window.mainloop()