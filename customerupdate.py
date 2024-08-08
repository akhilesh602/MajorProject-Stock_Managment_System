import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def custupdate():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Customers')
    t.config(bg='plum3')
    
    lt=[]
    def fillcustid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select custid from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
    
    def update():
        if len(b1.get())==0 or len(d1.get())==0 or len(e1.get())==0 or len(f1.get())==0:
            messagebox.showinfo('hi','plss fill all data')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa3=b1.get()
            ab3=d1.get()
            ad3=e1.get()
            ae3=f1.get()
            sql3="update customers set cname='%s', phone='%s', email='%s' where custid='%s'"%(ab3,ad3,ae3,aa3)
            cur.execute(sql3)
            db.commit()
            db.close()
            messagebox.showinfo('Update','Data Updated')
        
        
    a=Label(t,text='Customer Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='plum3')
    a.place(x=280,y=30)
    
    b=Label(t,text='Customer id',font=('Monotype Corsiva',26),bg='plum3')
    b.place(x=100,y=150)
    b1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='plum3')
    fillcustid()
    b1['values']=lt
    b1.place(x=320,y=160)
    
    d=Label(t,text='Customer name',font=('Monotype Corsiva',26),bg='plum3')
    d.place(x=100,y=220)
    d1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    d1.place(x=320,y=230)
    
    e=Label(t,text='Contact no.',font=('Monotype Corsiva',26),bg='plum3')
    e.place(x=100,y=290)
    e1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    e1.place(x=320,y=300)
    
    f=Label(t,text='Email',font=('Monotype Corsiva',26),bg='plum3')
    f.place(x=100,y=370)
    f1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    f1.place(x=320,y=380)
    
    bt=Button(t,text='Update',bd=5,font=1,bg='light slate gray',fg='spring green',command=update)
    bt.place(x=330,y=500)
    
    t.mainloop()
