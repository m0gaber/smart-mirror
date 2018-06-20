##################### check.py ###########################
from Tkinter import *
import tkMessageBox

master = Tk()





def check_btn1():
   if var1.get() == 1:
         return 1
   else :
      return 0

def check_btn2():
   if var2.get() == 1:
         return 2
   else :
      return 0

def check_btn3():
   if var3.get() == 1:
         return 3
   else :
      return 0

def check_btn4():
   if var4.get() == 1:
         return 4
   else :
      return 0

master.configure(background='black')
Label(master, text="Your Choices:",bg="black",fg="white",font=('Helvetica',20)).grid(row=0, sticky=W)


var1 = IntVar()
var1.set(0)
Checkbutton(master, text="Email", variable=var1,command=check_btn1,height=3,width=10,font=('Helvetica',30),bg="black",fg="white",selectcolor="black").grid(row=1, sticky=W)


var2 = IntVar()
var2.set(0)
Checkbutton(master, text="Clock", variable=var2,command=check_btn2,height=3,width=10,font=('Helvetica',30),bg="black",fg="white",selectcolor="black").grid(row=2, sticky=W)


var3 = IntVar()
var3.set(0)
Checkbutton(master, text="Weather", variable=var3,command=check_btn3,height=3,width=10,font=('Helvetica',30),bg="black",fg="white",selectcolor="black").grid(row=2,column =2, sticky=W)


var4 = IntVar()
var4.set(0)
Checkbutton(master, text="News", variable=var4,command=check_btn4,height=3,width=10,font=('Helvetica',30),bg="black",fg="white",selectcolor="black").grid(row=1,column =2, sticky=W)




Button(master, text='Submit', command=master.destroy,height=3,width=10,font=('Helvetica',20),bg="black",fg="white").grid(row=6, sticky=W)

mainloop()
