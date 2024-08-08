import tkinter
from tkinter import *
import pymysql

from mainscreen import *

def admin():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Admin')
    t.resizable(width=False, height=False)
    d=Canvas(t,height=800,width=800,bg='gray20')
    d.place(x=0,y=0)
    d.create_rectangle(100,130,680,600,outline='lavender',width=3,fill='gray38')
    
    def adminlogin():
        if len(b1.get())==0 or len(d1.get())==0:
               messagebox.showwarning('Fill-up','Please fill all details')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa=b1.get()
            ab=d1.get()
            sql="select count(0)  from admintable where adminid='%s' and adminpassword='%s'"%(aa,ab)
            cur.execute(sql)
            data=cur.fetchone()
            b1.delete(0,100)
            d1.delete(0,100)
            if data[0]==0:
                messagebox.showwarning('Incorrect Password','Please Enter Correct Password')
            else:
               mainscreen()
           
    def cancel():
        t.destroy()
    
    a=Label(t,text='Admin  Info',fg='red',font=('Lucida Calligraphy',28,UNDERLINE),bg='gray20')
    a.place(x=280,y=40)
    
    b=Label(t,text='Admin id',font=('Monotype Corsiva',26),bg='gray38',fg='lavender')
    b.place(x=150,y=200)
    b1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='blue',bg='gray48',bd=4)
    b1.place(x=320,y=205)
    
    d=Label(t,text='Password',font=('Monotype Corsiva',26),bg='gray38',fg='lavender')
    d.place(x=150,y=330)
    d1=Entry(t,width=25,show='*',font=("Comic Sans MS", 14,"bold"),fg='lavender',bg='gray48',bd=5)
    d1.place(x=320,y=335)
    
    bt=Button(t,text='Log In',bd=5,font=('Times New Roman',17),width=10,bg='light slate gray',fg='cyan',command=adminlogin)
    bt.place(x=325,y=430)
    
    bt=Button(t,text='Cancel',bd=5,font=('Times New Roman',17),width=10,bg='light slate gray',fg='firebrick',command=cancel)
    bt.place(x=325,y=515)
    t.mainloop()