from tkinter import *  
import random
root = Tk()  

Label(root, text="Roll the dice!").grid(row=0,column=20)

lbl=Label(root, text="image here")
lbl.grid(row=1,column=20)

def roll():
    x=random.randrange(1,6,1)
    if x==1:
        pic=PhotoImage(file="d1.png")
    elif x==2:
        pic=PhotoImage(file="d2.png")
    elif x==3:
        pic=PhotoImage(file="d3.png")
    elif x==4:
        pic=PhotoImage(file="d4.png")
    elif x==5:
        pic=PhotoImage(file="d5.png")
    elif x==6:
        pic=PhotoImage(file="d6.png")
    lbl=Label(root,image=pic)
    lbl.grid(row=1,column=20)
    b1.invoke()

b1=Button(root,text='Roll it!',width=25,command=roll,fg='red')
b1.grid(row=40,column=20)

root.mainloop()  