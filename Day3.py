from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Registration Screen")
window.geometry('300x300')
window.configure(background = "green");
Firstname = Label(window ,text = "First Name").grid(row = 0,column = 0)
LastName = Label(window ,text = "Last Name").grid(row = 1,column = 0)
Email = Label(window ,text = "Email Id").grid(row = 2,column = 0)
Mobile = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
Firstname1 = Entry(window).grid(row = 0,column = 1)
Lastname1 = Entry(window).grid(row = 1,column = 1)
Email1 = Entry(window).grid(row = 2,column = 1)
Mobile1 = Entry(window).grid(row = 3,column = 1)
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=4,column=0)
window.mainloop()
