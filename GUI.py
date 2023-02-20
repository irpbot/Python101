from tkinter import *
from tkinter import ttk #theme of ttk
from tkinter import messagebox
import tkinter as tk

GUI = Tk() #หน้าจอหลักโปรแกรม
GUI.title('ถาม-ตอบภาษาอังกฤษ') #ชื่อ ttitle
GUI.geometry('500x400') #ขนาดโปรแกรม

L1 = Label(GUI,text='ถาม-ตอบภาษาอังกฤษ',font=('Angsana New',30),fg='black',bg="blue") #ข้อความลอย
L1.place(x=80,y=10)  #ตำแหน่ง x y


#############################
def Button1():
    text = 'yellow'
    messagebox.showinfo('สีเหลือง',text) #ชื่อไตเติล
    datetime.now()

FB1 = Frame(GUI)  #คล้ายกระดาน
FB1.place(x=50,y=100) 
B1 = ttk.Button(FB1,text='สีเหลือง',command=Button1)
B1.pack(ipadx=20,ipady=10) #ipad ปรับขนาด x y
#############################
def Button2():
    text = 'mango'
    messagebox.showinfo('มะม่วง',text) #ชื่อไตเติล
    datetime.now()

FB1 = Frame(GUI)  #คล้ายกระดาน
FB1.place(x=230,y=100) 
B1 = ttk.Button(FB1,text='มะม่วง',command=Button2)
B1.pack(ipadx=20,ipady=10) #ipad ปรับขนาด x y
#############################
def Button3():
    text = 'อั่งโล่'
    messagebox.showinfo('เตา',text) #ชื่อไตเติล
    datetime.now()

FB1 = Frame(GUI)  #คล้ายกระดาน
FB1.place(x=50,y=200) 
B1 = ttk.Button(FB1,text='เตา',command=Button3)
B1.pack(ipadx=20,ipady=10) #ipad ปรับขนาด x y
#############################
def Button4():
    text = 'อีโต้'
    messagebox.showinfo('มีด',text) #ชื่อไตเติล
    datetime.now()

FB1 = Frame(GUI)  #คล้ายกระดาน
FB1.place(x=230,y=200) 
B1 = ttk.Button(FB1,text='มีด',command=Button4)
B1.pack(ipadx=20,ipady=10) #ipad ปรับขนาด x y
#############################

GUI.mainloop()
