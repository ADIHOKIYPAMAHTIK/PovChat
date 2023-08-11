#ВВод библиотек
from tkinter import *
import tkinter.messagebox
import random

#Создание окна, означение геометрии и её блокировка
window = Tk()
window.title("PovChat")
window.geometry('400x300')
window.minsize(400, 300)
window.maxsize(400, 300)


#Создание виджетов
entry = Entry(window, width=57, bd=5, bg='green')
entry.pack(side=LEFT)
button = Button(window,text='Send',width=5,height=1,bg='red',fg='black',font='arial 8', activebackground='gray', relief='solid')
button.pack(side=RIGHT)
window.mainloop()