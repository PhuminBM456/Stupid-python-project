from tkinter import *
import tkinter.messagebox
import random

root = Tk()
root.title("แอพหาคู่")
root.geometry("900x600+600+200")

def Submit():
    rand = random.randint(1,500)

    t1 = name.get()
    # t2 = specie.get()
    t3 = spec.get()

    if t1 == "":
        tkinter.messagebox.showinfo("Error","กรุณาใส่ชื่อของคุณ")
    # elif t2 == "":
    #     tkinter.messagebox.showinfo("Error","กรุณาใส่เผ่าพันธุ์ของคุณ")
    elif t3 == "":
        tkinter.messagebox.showinfo("Error","กรุณาใส่สเปคของคุณ")
    else:
        sex = False

        f = open("name.txt", "r")
        specie = f.read().split(",")
        choose = random.randint(0,len(specie)-1)

        if rand % 2 == 0:
            sex = "ชาย"
        else:
            sex = "หญิง"

        prod.config(text="สเปคของคุณ คือ "+specie[choose]+" เพศ"+sex+" อายุ"+str(rand)+"ปี",fg="blue",font=("Arial", 25),bg="yellow")

        # prod.config(text="สเปคของคุณ คือ "+t2+" เพศ"+sex+" อายุ"+str(rand)+"ปี",fg="blue",font=("Arial", 25),bg="yellow")

label1 = Label(text="แอพหาคู่",fg="blue",font=("Arial", 30),bg="pink")
label1.pack(pady=10)

label2 = Label(text="ชื่อ",fg="blue",font=("Arial", 20),bg="pink")
label2.pack(pady=10)

name = StringVar()
kb1 = Entry(textvariable=name,width=30,font=("Arial", 20))
kb1.pack(pady=10)

# label3 = Label(text="เผ่าพันธุ์",fg="blue",font=("Arial", 20),bg="pink")
# label3.pack(pady=10)

# specie = StringVar()
# kb2 = Entry(textvariable=specie,width=30,font=("Arial", 20))
# kb2.pack(pady=10)

label4 = Label(text="สเปค",fg="blue",font=("Arial", 20),bg="pink")
label4.pack(pady=10)

spec = StringVar()
kb3 = Entry(textvariable=spec,width=30,font=("Arial", 20))
kb3.pack(pady=10)

btn = Button(text="เสร็จสิ้น",fg="white",bg="red",font=("Arial", 15),command=Submit)
btn.pack()

prod = Label(text="")
prod.pack(pady=10)


root.mainloop()
