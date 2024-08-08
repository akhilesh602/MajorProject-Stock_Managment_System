import tkinter
from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
def ordersdelete():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Orders')
    t.config(bg='LavenderBlush3')
    
    lt=[]
    def fillorderid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select orderid from orders"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
    
    def delete():
        if len(b1.get())==0:
            messagebox.showinfo('hi','plss fill order id')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa2=b1.get()
            sql2="delete from orders where orderid='%s'"%(aa2)
            cur.execute(sql2)
            db.commit()
            db.close()
            messagebox.showinfo('Delete','Data Deleted')
        
    def Search():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        aa1=b1.get()
        sql1="select * from orders where orderid='%s'"%(aa1)
        cur.execute(sql1)
        data=cur.fetchone()
        d1.config(text=' ')
        e1.config(text=' ')
        f1.config(text=' ')
        g1.config(text=' ')
        h1.config(text=' ')
        d1.config(text=data[1])
        e1.config(text=data[2])
        f1.config(text=data[3])
        g1.config(text=data[4])
        h1.config(text=data[5])
        db.close()
        
    a=Label(t,text='Orders Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='LavenderBlush3')
    a.place(x=280,y=30)
    
    b=Label(t,text='Order id',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    b.place(x=150,y=150)
    b1=ttk.Combobox(t,width=10,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillorderid()
    b1['values']=lt
    b1.place(x=440,y=160)
    
    d=Label(t,text='Customer id',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    d.place(x=150,y=220)
    d1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='LavenderBlush3',bd=4)
    d1.place(x=350,y=225)
    
    e=Label(t,text='Item id',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    e.place(x=150,y=290)
    e1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='LavenderBlush3',bd=4)
    e1.place(x=350,y=295)
    
    f=Label(t,text='Category id',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    f.place(x=150,y=360)
    f1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='LavenderBlush3',bd=4)
    f1.place(x=350,y=365)
    
    g=Label(t,text='Quantity',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    g.place(x=150,y=430)
    g1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='LavenderBlush3',bd=4)
    g1.place(x=350,y=435)
    
    h=Label(t,text='Date of Order',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    h.place(x=150,y=500)
    h1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='LavenderBlush3',bd=4)
    h1.place(x=350,y=505)
    
    bt=Button(t,text='Delete',bd=5,font=1,bg='light slate gray',fg='spring green',command=delete)
    bt.place(x=330,y=620)
    
    bts=Button(t,text='Search',bd=1,font=1,bg='lavender',fg='blue',command=Search)
    bts.place(x=650,y=155)
    t.mainloop()
