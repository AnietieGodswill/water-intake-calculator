#water intake calculator
import tkinter as tk
from tkinter import *
from plyer import notification
from time import sleep
import os 
root = Tk()
root.geometry("350x300")
root.title("Water Intake Calculator")
notification.notify(app_icon = os.getcwd()+"\water.ico")
#app.iconbitmap('icon.ico')
def AgeBelow5():
    val = 100
    while (val<=1500):                                                                                         
        tol = "Drink:100 ml\n"
        showtol = "Drank: %s ml out of 1500 ml" %(val)
        notification.notify(title = "Water Intake Calculator",message = tol+showtol,timeout = 15)
        val += 100
        sleep(3600)

def AgeBelow10():
    val = 100
    while (val<=3000):                                                                                         
        tol = "Drink:100 ml\n"
        showtol = "Drank: %s ml out of 3000 ml" %(val)
        notification.notify(title = "Water Intake Calculator",message = tol+showtol,timeout = 15)
        val += 100
        sleep(3600)
def AgeBelow20():
    val = 100
    while (val<=4000):                                                                                         
        tol = "Drink:100 ml\n"
        showtol = "Drank: %s ml out of 4000 ml" %(val)
        notification.notify(title = "Water Intake Calculator",message = tol+showtol,timeout = 15)
        val += 100
        sleep(3600)
def AgeBelow60():
    val = 100
    while (val<=5000):                                                                                         
        tol = "Drink:100 ml\n"
        showtol = "Drank: %s ml out of 5000 ml" %(val)
        notification.notify(title = "Water Intake Calculator",message = tol+showtol,timeout = 15)
        val += 100
        sleep(3600)
def AgeAbove60():
    val = 100
    while (val<=3000):                                                                                         
        tol = "Drink:100 ml\n"
        showtol = "Drank: %s ml out of 3000 ml" %(val)
        notification.notify(title = "Water Intake Calculator",message = tol+showtol,timeout = 15)
        val += 100
        sleep(3600)


Label(root,text="Water Intake Calculator", font='helvetica 14 bold').grid(row=0,column=1)
Label(root,text="Select Age To Start:- ", font='helvetica 14 italic').grid(row=1,column=1)
Button(root, width=20,text="1 to 5 years", font=('helvetica',14),bg='green', fg='white',command=AgeBelow5,borderwidth=4).grid(row=2,column=1)
Button(root, width=20,text="5 to 10 years", font=('helvetica',14),bg='green', fg='white',command=AgeBelow10,borderwidth=4).grid(row=3,column=1)
Button(root, width=20,text="10 to 20 years", font=('helvetica',14),bg='green', fg='white',command=AgeBelow20,borderwidth=4).grid(row=4,column=1)
Button(root, width=20,text="20 to 60 years", font=('helvetica',14),bg='green', fg='white',command=AgeBelow60,borderwidth=4).grid(row=5,column=1)
Button(root, width=20,text="Above 60 years", font=('helvetica',14),bg='green', fg='white',command=AgeAbove60,borderwidth=4).grid(row=6,column=1)
Label(root,text="Developed By: Nishant Tiwari (dx4iot)", font='helvetica 14 bold').grid(row=7,column=1)


root.mainloop() 
