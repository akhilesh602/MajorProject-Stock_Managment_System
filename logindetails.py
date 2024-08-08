
import tkinter
from tkinter import *
import pymysql
from userscreen import *
from userregister import *
from forgot import *
def user():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Login')
    t.resizable(width=False, height=False)
    d=Canvas(t,height=800,width=800,bg='gray20')
    d.place(x=0,y=0)
    d.create_rectangle(100,170,700,310,outline='lavender',width=3,fill='gray38')
    d.create_rectangle(250,330,545,750,outline='lavender',width=3,fill='gray38')
    d.create_line(545,390,545,750,width=3,fill='royalblue')
    d.create_line(320,750,545,750,width=3,fill='royalblue')
    d.create_line(250,330,485,330,width=3,fill='royalblue')
    d.create_line(250,330,250,690,width=3,fill='royalblue')
    def login():
        if len(b1.get())==0 or len(d1.get())==0:
               messagebox.showwarning('Fill-up','Please fill all details')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa=b1.get()
            ab=d1.get()
            sql="select count(0)  from usertable where userid='%s' and password='%s'"%(aa,ab)
            cur.execute(sql)
            data=cur.fetchone()
            b1.delete(0,100)
            d1.delete(0,100)
            if data[0]==0:
                messagebox.showinfo('Incorrect Password','Please Enter Correct Password')
            else:
                userscreen()
            
    def cancel():
        t.destroy()
    
    a=Label(t,text='User Info',fg='red',font=('Lucida Calligraphy',28,UNDERLINE),bg='gray20')
    a.place(x=300,y=50)
    
    b=Label(t,text='User id',font=('Monotype Corsiva',22),bg='gray38',fg='lavender')
    b.place(x=150,y=180)
    b1=Entry(t,width=30,fg='royalblue',font=('Arial Rounded MT Bold',14),bd=5,bg='MistyRose')
    b1.place(x=320,y=195)
    
    d=Label(t,text='Password',font=('Monotype Corsiva',22),bg='gray38',fg='lavender')
    d.place(x=150,y=240)
    d1=Entry(t,width=30,show='*',fg='red',font=14,bd=5,bg='peachpuff')
    d1.place(x=320,y=255)
    
    bt=Button(t,text='Log In',bd=5,font=('Times New Roman',17),bg='light slate gray',fg='cyan',command=login)
    bt.place(x=280,y=425)
    
    bt1=Button(t,text='Cancel',bd=5,font=('Times New Roman',17),bg='light slate gray',fg='firebrick',command=cancel)
    bt1.place(x=400,y=425)
    
    bt2=Button(t,text='New Registration',bd=5,font=('Times New Roman',17),bg='light slate gray',fg='cyan',command=signup)
    bt2.place(x=300,y=550)
    
    bt3=Button(t,text='Forgot Password',bd=5,font=('Times New Roman',17),bg='light slate gray',fg='firebrick',command=forgotid)
    bt3.place(x=300,y=650)
    t.mainloop()
