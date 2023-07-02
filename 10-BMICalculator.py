from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.geometry("400x400")
window.resizable(False,False)
window.config(pady=50)

result_label = Label()


def control():
    input_weight = weight_entry.get().strip() #boşlukları tırpalamak
    input_height = height_entry.get().strip() #boşlukları tırpalamak
    if input_weight == "" or input_height == "":
        result_label.config(text="Değerler boş bırakılamaz.")
        result_label.pack()
    else:
        calculate_BMI()



def calculate_BMI():
    try:
        input_weight=int(weight_entry.get())
        input_height=int(height_entry.get())
        BMI=round((input_weight/((input_height**2)/10000)),2)
        print(BMI)

        if BMI <= 18.5:
            result = f"Çok Zayıf - BMI:{BMI}"
        elif 18.5 < BMI < 24.9:
            result = f"Normal - BMI:{BMI}"
        elif 25.0 < BMI < 29.9:
            result = f"Obez Adayı - BMI:{BMI}"
        elif 30.0 < BMI < 34.9:
            result = f"1. Derece Obez - BMI:{BMI}"
        elif 35.0 < BMI < 39.9:
            result = f"2. Derece Obez - BMI:{BMI}"
        elif 40.0 < BMI:
            result = f"3. Derece Obez - BMI:{BMI}"
        else:
            result = "HATA"

        result_label.config(text=result)
        result_label.pack()
    except:
        result_label.config(text="Girdiğiniz değerler uygun değil")




weight_label = Label(text="Kilonuzu Giriniz (kg)")
weight_label.pack()
weight_entry = Entry()
weight_entry.pack()


height_label = Label(text="Boyunuzu Giriniz (cm)")
height_label.pack()
height_entry = Entry()
height_entry.pack()


calculate_button = Button(text="Hesapla",command=control)
calculate_button.pack()





window.mainloop()