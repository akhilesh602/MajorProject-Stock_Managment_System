import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql

def signup():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('userregister')
    t.config(bg='pink3')
    def login():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        aa2=g1.get()
        sql="select count(0)  from usertable where userid='%s'"%(aa2)
        cur.execute(sql)
        data=cur.fetchone()
        
        
        if data[0]==0:
            def insert():
                if len(b1.get())==0 or len(d1.get())==0 or len(e1.get())==0 or len(f1.get())==0 or len(g1.get())==0 or len(h1.get())==0:
                    messagebox.showinfo('hi','plss fill all data')
                elif j1.get()!=h1.get():
                    messagebox.showinfo('warning','Password and Confirm Password are not same')
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
                    cur=db.cursor()
                    aa=b1.get()
                    ab=d1.get()
                    ac=e1.get()
                    ad=(f1.get())
                    ae=(g1.get())
                    af=(h1.get())
                    ag=(j1.get())
                    sql="insert into usertable values('%s','%s','%s','%s','%s','%s')"%(aa,ab,ac,ad,ae,af)
                    cur.execute(sql)
                    db.commit()
                    
                    b1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    f1.delete(0,100)
                    g1.delete(0,100)
                    h1.delete(0,100)
                    j1.delete(0,100)
                    db.close()
                    messagebox.showinfo('Insert','you are successfully registrate....kindly login')
        else:
            messagebox.showinfo('oops','this userid is already exits, kindly try with another userid')
            b1.delete(0,100)
            d1.delete(0,100)
            e1.delete(0,100)
            f1.delete(0,100)
            g1.delete(0,100)
            h1.delete(0,100)
            j1.delete(0,100)
            
    def cancel():
        t.destroy()
    
    a=Label(t,text='User Register',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='pink3')
    a.place(x=280,y=30)
    
    b=Label(t,text='Name',font=('Monotype Corsiva',26),bg='pink3')
    b.place(x=120,y=150)
    b1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4 )
    b1.place(x=350,y=160)
    
    d=Label(t,text='Address',font=('Monotype Corsiva',26),bg='pink3')
    d.place(x=120,y=220)
    d1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    d1.place(x=350,y=230)
    
    e=Label(t,text='Phone',font=('Monotype Corsiva',26),bg='pink3')
    e.place(x=120,y=290)
    e1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    e1.place(x=350,y=300)
    
    f=Label(t,text='Email',font=('Monotype Corsiva',26),bg='pink3')
    f.place(x=120,y=370)
    f1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    f1.place(x=350,y=380)
    
    g=Label(t,text='User Id',font=('Monotype Corsiva',26),bg='pink3')
    g.place(x=120,y=440)
    g1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    g1.place(x=350,y=450)
    
    h=Label(t,text='Password',font=('Monotype Corsiva',26),bg='pink3')
    h.place(x=120,y=520)
    h1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='red',bg='aquamarine2',bd=4)
    h1.place(x=350,y=530)
    
    j=Label(t,text='Confirm Password',font=('Monotype Corsiva',26),bg='pink3')
    j.place(x=100,y=600)
    j1=Entry(t,width=25,show='*',font=("Comic Sans MS", 14,"bold"),fg='red',bg='aquamarine2',bd=4)
    j1.place(x=350,y=610)
    
    bt=Button(t,text='Save',bd=5,font=1,bg='light slate gray',fg='spring green',command=login)
    bt.place(x=330,y=700)
    
    bts=Button(t,text='Cancel',bd=5,font=1,bg='DarkSlateGray3',fg='blue',command=cancel)
    bts.place(x=450,y=700)
    t.mainloop()
