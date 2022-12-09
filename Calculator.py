from tkinter import *

obj=Tk()
obj.title('Calculator')
obj.geometry('600x400')
obj.iconbitmap('icons8-apple-logo-16 (1).ico')


lbl1=Label(obj,text='Value 1 :',fg='red')
lbl1.place(x=200,y=100)
e1=Entry(obj,bg='yellow')
e1.place(x=250,y=100)

lbl2=Label(obj,text='Value 2 :',fg='red')
lbl2.place(x=200,y=130)
e2=Entry(obj,bg='yellow')
e2.place(x=250,y=130)

lbl3=Label(obj,text='',fg='purple')
lbl3.place(x=270,y=200)


def add():
    lbl3.config(text='Sum is : '+str(eval(e1.get())+eval(e2.get())))

def min():
    lbl3.config(text='Subtraction is : '+str(eval(e1.get())-eval(e2.get())))

def product():
    lbl3.config(text='Multiplication is : '+str(eval(e1.get())*eval(e2.get())))

def division():
    lbl3.config(text='Division is : '+str(eval(e1.get())/eval(e2.get())))


sum=Button(obj,text='+',command=add,bg='yellow',fg='red',activebackground='black',activeforeground='purple')
sum.place(x=250,y=160)

sub=Button(obj,text='-',command=min,bg='yellow',fg='red',activebackground='black',activeforeground='purple')
sub.place(x=280,y=160)

mul=Button(obj,text='*',command=product,bg='yellow',fg='red',activebackground='black',activeforeground='purple')
mul.place(x=310,y=160)

div=Button(obj,text='/',command=division,bg='yellow',fg='red',activebackground='black',activeforeground='purple')
div.place(x=340,y=160)


obj.mainloop()
