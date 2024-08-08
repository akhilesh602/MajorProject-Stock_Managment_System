import tkinter
from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
def suppfind():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Supplier')
    t.config(bg='dark khaki')
    
    lt=[]
    def fillsupplierid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select supplierid from supplier"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
    
    def find():
        if len(b1.get())==0:
            messagebox.showinfo('hi','plss fill supplier id')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa1=b1.get()
            sql1="select * from supplier where supplierid='%s'"%(aa1)
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
            messagebox.showinfo('Find','Data Found')
        
        
    a=Label(t,text='Supplier Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='dark khaki')
    a.place(x=280,y=30)
    
    b=Label(t,text='Supplier id',font=('Monotype Corsiva',26),bg='dark khaki')
    b.place(x=150,y=150)
    b1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillsupplierid()
    b1['values']=lt
    b1.place(x=350,y=160)
    
    d=Label(t,text='Supplier Name',font=('Monotype Corsiva',26),bg='dark khaki')
    d.place(x=150,y=220)
    d1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='dark khaki',bd=4)
    d1.place(x=350,y=225)
    
    e=Label(t,text='Address',font=('Monotype Corsiva',26),bg='dark khaki')
    e.place(x=150,y=290)
    e1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='dark khaki',bd=4)
    e1.place(x=350,y=295)
    
    f=Label(t,text='Email',font=('Monotype Corsiva',26),bg='dark khaki')
    f.place(x=150,y=360)
    f1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='dark khaki',bd=4)
    f1.place(x=350,y=365)
    
    g=Label(t,text='Contact Info',font=('Monotype Corsiva',26),bg='dark khaki')
    g.place(x=150,y=430)
    g1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='dark khaki',bd=4)
    g1.place(x=350,y=435)
    
    h=Label(t,text='Category id',font=('Monotype Corsiva',26),bg='dark khaki')
    h.place(x=150,y=500)
    h1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='dark khaki',bd=4)
    h1.place(x=350,y=505)
    
    bt=Button(t,text='Find',bd=5,font=1,bg='DarkSlateGray1',fg='blue',command=find)
    bt.place(x=330,y=620)
    
    
    t.mainloop()


        
    