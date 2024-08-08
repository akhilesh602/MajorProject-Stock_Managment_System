import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def ordersupdate():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Orders')
    t.config(bg='LavenderBlush3')
    
    lt1=[]
    def fillorderid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select orderid from orders"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt1.append(res[0])
            
    lt2=[]
    def fillcustid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select custid from orders"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt2.append(res[0])
            
    lt3=[]
    def fillitemid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select itemid from orders"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt3.append(res[0])
            
    lt4=[]
    def fillcatid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select catid from orders"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt4.append(res[0])
    
    def update():
        if len(b1.get())==0 or len(d1.get())==0 or len(e1.get())==0 or len(f1.get())==0 or len(g1.get())==0 or len(h1.get())==0:
            messagebox.showinfo('hi','plss fill all data')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa3=b1.get()
            ab3=d1.get()
            ad3=e1.get()
            ae3=f1.get()
            af3=int(g1.get())
            ag3=h1.get()
            sql3="update orders set custid='%s', itemid='%s', catid='%s', qty='%d', dateoforder='%s' where orderid='%s'"%(ab3,ad3,ae3,af3,ag3,aa3)
            cur.execute(sql3)
            db.commit()
            db.close()
            messagebox.showinfo('Update','Data Updated')
            
       
        
    a=Label(t,text='Orders Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='LavenderBlush3')
    a.place(x=280,y=30)
    
    b=Label(t,text='Order id',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    b.place(x=120,y=150)
    b1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillorderid()
    b1['values']=lt1
    b1.place(x=350,y=160)
    
    d=Label(t,text='Customerid id',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    d.place(x=120,y=220)
    d1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillcustid()
    d1['values']=lt2
    d1.place(x=350,y=230)
    
    e=Label(t,text='Item id',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    e.place(x=120,y=290)
    e1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillitemid()
    e1['values']=lt3
    e1.place(x=350,y=300)
    
    f=Label(t,text='Category id',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    f.place(x=120,y=370)
    f1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='lavender',background='peachpuff')
    fillcatid()
    f1['values']=lt4
    f1.place(x=350,y=380)
    
    g=Label(t,text='Quantity',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    g.place(x=120,y=440)
    g1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    g1.place(x=350,y=450)
    
    h=Label(t,text='Date of Order',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    h.place(x=120,y=520)
    h1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    h1.place(x=350,y=530)
    
    bt=Button(t,text='Update',bd=5,font=1,bg='light slate gray',fg='spring green',command=update)
    bt.place(x=330,y=650)
    
    
    t.mainloop()


