from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Employee Details")
window.geometry('400x400')
window.configure(background = "yellow");
Empname = Label(window ,text = "Employee Name").grid(row = 0,column = 0)
Empid= Label(window ,text = "Employee ID").grid(row = 1,column = 0)
Empadd= Label(window ,text = "Employee Address").grid(row = 2,column = 0)
EmpDOB= Label(window ,text = "Employee DOB").grid(row = 3,column = 0)
Gender=Label(window ,text = "Gender").grid(row = 4,column = 0)
EmpMobile = Label(window ,text = "Contact Number").grid(row = 6,column = 0)
Empemail=Label(window ,text = "Email").grid(row = 7,column = 0)
Empposition=Label(window ,text = "Position").grid(row = 8,column = 0)
Empcity=Label(window ,text = "Employee City").grid(row = 9,column = 0)
Empstate=Label(window ,text = "Employee State").grid(row = 10,column = 0)
Empcountry=Label(window ,text = "Employee Country").grid(row = 11,column = 0)
Empdays=Label(window ,text = "Employee Days").grid(row = 12,column = 0)
Empname1 = Entry(window).grid(row = 0,column = 1)
Empid1 = Entry(window).grid(row = 1,column = 1)
Empadd1 = Entry(window).grid(row = 2,column = 1)
EmpDOB1 = Entry(window).grid(row = 3,column = 1)
EmpMobile1 = Entry(window).grid(row = 6,column = 1)
Empemail1 = Entry(window).grid(row = 7,column = 1)
Empposition1 = Entry(window).grid(row = 8,column = 1)
Empcity1 = Entry(window).grid(row = 9,column = 1)
Empstate1 = Entry(window).grid(row = 10,column = 1)
Empcountry1 = Entry(window).grid(row = 11,column = 1)
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=15,column=1)
var=IntVar()
Radiobutton(window,text="Male",padx= 5,variable=var,value=1,).grid(row=4,column=1)
Radiobutton(window,text="Female",padx=25,variable=var,value=2,).grid(row=5,column=1)
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
s=StringVar()
droplist=OptionMenu(window,s, *days)
droplist.config(width=15)
droplist.grid(row=12,column=1)
window.mainloop()