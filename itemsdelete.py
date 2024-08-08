import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def itemsdelete():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Items')
    t.config(bg='MistyRose2')
    
    lt=[]
    def fillitemid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select itemid from items"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
    
    def delete():
        if len(b1.get())==0:
            messagebox.showinfo('hi','plss fill item id')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa2=b1.get()
            sql2="delete from items where itemid='%s'"%(aa2)
            cur.execute(sql2)
            db.commit()
            db.close()
            messagebox.showinfo('Delete','Data Deleted')
            
    def Search():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        aa1=b1.get()
        sql1="select * from items where itemid='%s'"%(aa1)
        cur.execute(sql1)
        data=cur.fetchone()
        d1.config(text=' ')
        e1.config(text=' ')
        f1.config(text=' ')
        g1.config(text=' ')
        h1.config(text=' ')
        j1.config(text=' ')
        d1.config(text=data[1])
        e1.config(text=data[2])
        f1.config(text=data[3])
        g1.config(text=data[4])
        h1.config(text=data[5])
        j1.config(text=data[6])
        db.close()
            
        
    a=Label(t,text='Items Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='MistyRose2')
    a.place(x=280,y=30)
    
    b=Label(t,text='Item id',font=('Monotype Corsiva',26),bg='MistyRose2')
    b.place(x=150,y=150)
    b1=ttk.Combobox(t,width=10,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillitemid()
    b1['values']=lt
    b1.place(x=440,y=160)
    
    d=Label(t,text='Category id',font=('Monotype Corsiva',26),bg='MistyRose2')
    d.place(x=150,y=220)
    d1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='MistyRose2',bd=4)
    d1.place(x=350,y=225)
    
    e=Label(t,text='Item name',font=('Monotype Corsiva',26),bg='MistyRose2')
    e.place(x=150,y=290)
    e1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='MistyRose2',bd=4)
    e1.place(x=350,y=295)
    
    f=Label(t,text='Unit',font=('Monotype Corsiva',26),bg='MistyRose2')
    f.place(x=150,y=360)
    f1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='MistyRose2',bd=4)
    f1.place(x=350,y=365)
    
    g=Label(t,text='Price',font=('Monotype Corsiva',26),bg='MistyRose2')
    g.place(x=150,y=430)
    g1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='MistyRose2',bd=4)
    g1.place(x=350,y=435)
    
    h=Label(t,text='Open Quantity',font=('Monotype Corsiva',26),bg='MistyRose2')
    h.place(x=150,y=500)
    h1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='MistyRose2',bd=4)
    h1.place(x=350,y=505)
    
    j=Label(t,text='Current Quantity',font=('Monotype Corsiva',26),bg='MistyRose2')
    j.place(x=130,y=570)
    j1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='MistyRose2',bd=4)
    j1.place(x=350,y=575)
    
    bt=Button(t,text='Delete',bd=5,font=1,bg='dim gray',fg='cyan',command=delete)
    bt.place(x=330,y=650)
    
    bts=Button(t,text='Search',bd=1,font=1,bg='lavender',fg='blue',command=Search)
    bts.place(x=650,y=155)
    t.mainloop()
