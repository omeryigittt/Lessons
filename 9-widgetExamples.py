from tkinter import *
# bu şekilde de her şey içeri alınabilir bu sayede
# window = tkinter.Tk() böyle yazmak yerine
window = Tk() # yazılabilir
window.title("Deneme")
window.minsize(width=600,height=600)
window.config(padx=20,pady=20)

my_label = Label(text="My Label")
my_label.config(bg="black")
my_label.config(fg="white")
my_label.pack()

def button_clicked():
    input_text=my_text.get("1.0",END)
    # "1.0" 1: Başlayacağı satır
    #       2: Başlayacağı karakter
    # END: biteceği yer tkinterin fonksiyonu aslında
    # ve yukarıda herşeyi import ettiğimizden sadece END ile çağırabildik
    # öyle olmasaydı. tkinter.END ile çağırmamaız gerekecekti.
    print(input_text)


my_button = Button(text="Buton", command=button_clicked)
my_button.pack()


my_text = Text(width=50,height=10)
my_text.focus()
my_text.pack()


#scale
def scale_selected(value):
    print(value)

my_scale = Scale(from_=0,to=50,command=scale_selected)
my_scale.pack()

# spinbox
def spinbox_selected():
    print(my_spinbox.get())


my_spinbox = Spinbox(from_=0,to=50,command=spinbox_selected)
my_spinbox.pack()

#checkbutton
def checkbutton_selected():
    print(my_check_state.get())


my_check_state = IntVar() # tkinter fonksiyonu: seçili ise 1 değilse 0 alır
my_checkbutton = Checkbutton(text="Seçin",variable=my_check_state,command=checkbutton_selected)
my_checkbutton.pack( )


# radio button
def radio_selected():
    print(my_radioButton_state.get())

my_radioButton_state = IntVar()

my_radio_button = Radiobutton(text="1. seçenek", value=10, variable=my_radioButton_state, command=radio_selected)
my_radio_button_2 = Radiobutton(text="2. seçenek", value=20, variable=my_radioButton_state, command=radio_selected)
my_radio_button.pack()
my_radio_button_2.pack()


# listbox
def listbox_selected(event):
    # listbox bu şekilde kullanıcı aksiyonu bekler
    # curselected : tıklanan değerdir.
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
name_list = ["ömer", "yiğit", "Ela", "Sarı" ,"Fadime", "Yusuf"]
for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])
    # my liste ögeler bu fonksiyon ile sokulur
    # ilk virgül kaçıncı indise sokulacağı, ikinci indis ise sokulacak değerdir.

# fonksiyona bağlama şekli de diğerlerinden farklıdır.
# direk configürasyon ayarı olarak yazdırmaz ile bind ile bağlamak gerekir.
# dahası saçma sapan yazı stilinde bi aksiyon tanımlama metni ister
# tutorialden bakılabilir.
my_listbox.bind('<<ListboxSelect>>',listbox_selected)
my_listbox.pack()












window.mainloop()

