from tkinter import *
l=Tk()
l.title("Real world")
b=Checkbutton(l,text="hello",fg="black",activebackground="blue")
b.pack(side="top")
b1=Button(l,text="welcome to the real world",fg="blue")
b1.pack(side="right")
b2=Button(l,text="mac",fg="purple")
b2.pack(side="top")
b3=Label(l,text="brabus")
b3.grid()
ei=Label(l,text="shake")
ei.grid()
l.mainloop()