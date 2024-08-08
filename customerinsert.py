import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
import re
def custinsert():
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
    
    def validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return True
        else:
            return False
        
    def insert():
        if len(b1.get())==0 or len(d1.get())==0 or len(e1.get())==0 or len(f1.get())==0:
            messagebox.showinfo('hi','plss fill all data')
            
        elif len(e1.get())!=10:
            messagebox.showerror('Fill-up','Please insert 10 digit number')
            
        else:
            if validate_email(f1.get()):
                db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
                cur=db.cursor()
                aa=b1.get()
                ab=d1.get()
                ac=e1.get()
                ad=f1.get()
                sql="insert into customers values('%s','%s','%s','%s')"%(aa,ab,ac,ad)
                cur.execute(sql)
                db.commit()
                b1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                db.close()
                messagebox.showinfo('Insert','Data is inserted in Customers')
            else:
                messagebox.showerror('hi','Invalid Email Id')
              
    def searchid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        aa2=b1.get()
        ab=d1.get()
        sql="select count(0)  from customers where custid='%s' "%(aa2)
        cur.execute(sql)
        data=cur.fetchone()
        b1.delete(0,100)
        if data[0]==0:
            messagebox.showinfo('Information','This id is not exits, you can insert it')
        else:
           messagebox.showerror('Information','This id is already exits please try with another one')
        
    
    def close():
        t.destroy()
        
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
    
    bt=Button(t,text='Insert',bd=5,font=1,bg='light slate gray',fg='spring green',command=insert)
    bt.place(x=280,y=500)
    
    bt1=Button(t,text='Close',bd=5,font=1,bg='light slate gray',fg='spring green',command=close)
    bt1.place(x=380,y=500)
    
    bt2=Button(t,text='Search',bd=4,font=1,bg='DarkSlateGray3',fg='blue',command=searchid)
    bt2.place(x=650,y=155)
    t.mainloop()
