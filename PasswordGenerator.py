from tkinter import *
from tkinter.ttk import *
import random
import pyperclip

win= Tk()
win.geometry('490x60')
win.title("Password Generator")

Password= StringVar()

def copy():
    pyperclip.copy(password)

def generate():
    global lower, upper, digits, password, list1
    a= int(combo.get())
    b= rb.get()
    lower= "abcdefghjiklmnopqrstuvwxyz"
    upper= "ABCDEFGHJIKLMNOPQRSTUVWXYZabcdefghjiklmnopqrstuvwxyz"
    digits= "ABCDEFGHJIKLMNOPQRSTUVWXYZabcdefghjiklmnopqrstuvwxyz0123456789!@#$%^&*()"
    password= ""

    for i in range(0, a):
        if b== '3':
            password= password + random.choice(digits)
        elif b== '2':
            password= password + random.choice(upper)
        elif b== '1':
           password= password + random.choice(lower)
    Password.set(password)


lbl1= Label(win, text= "Password", justify= 'left')
lbl1.grid(column= 0, row= 0)
lbl2= Label(win, text= "Length", justify= 'left')
lbl2.grid(column= 0, row= 1)



btn1= Button(win, text= "Copy", command= copy)
btn1.grid(column= 2, row= 0)
btn2= Button(win, text= "Generate", command= generate)
btn2.grid(column= 3, row= 0)


txt1= Entry(win, text= Password, width= 20)
txt1.grid(column= 1, row= 0)


combo= Combobox(win)
combo['values']= (8,9,10,11,12)
combo.grid(column= 1, row= 1)
combo.current(0)
combo.bind("<<ComboboxSelected>>")

rb= StringVar()
rb.set(2)
rad1= Radiobutton(win, text= "Low", value= '1', variable= rb)
rad1.grid(column= 2, row= 1)

rad2= Radiobutton(win, text= "Medium", value= '2', variable= rb)
rad2.grid(column= 3, row= 1)

rad3= Radiobutton(win, text= "Strong", value= '3', variable= rb)
rad3.grid(column= 4, row= 1)

win.mainloop()