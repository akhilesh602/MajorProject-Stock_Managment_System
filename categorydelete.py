import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def catdelete():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Category')
    t.config(bg='thistle3')
    
    lt=[]
    def fillcatid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select catid from category"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
    
    def delete():
        if len(b1.get())==0:
            messagebox.showinfo('hi','plss fill category id')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa2=b1.get()
            sql2="delete from category where catid='%s'"%(aa2)
            cur.execute(sql2)
            db.commit()
            db.close()
            messagebox.showinfo('Delete','Data Deleted')
            
    def search():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        aa1=b1.get()
        sql1="select * from category where catid='%s'"%(aa1)
        cur.execute(sql1)
        data=cur.fetchone()
        d1.config(text=' ')
        e1.config(text=' ')
        d1.config(text=data[1])
        e1.config(text=data[2])
        db.close()
        
        
    a=Label(t,text='Category Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='thistle3')
    a.place(x=270,y=30)
    
    b=Label(t,text='Category id',font=('Monotype Corsiva',26),bg='thistle3')
    b.place(x=180,y=150)
    b1=ttk.Combobox(t,width=10,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='peachpuff',background='peachpuff')
    fillcatid()
    b1['values']=lt
    b1.place(x=450,y=160)
    
    d=Label(t,text='Category name',font=('Monotype Corsiva',26),bg='thistle3')
    d.place(x=180,y=220)
    d1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='thistle3',bd=4)
    d1.place(x=370,y=230)
    
    e=Label(t,text='Description',font=('Monotype Corsiva',26),bg='thistle3')
    e.place(x=180,y=280)
    e1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='thistle3',bd=4)
    e1.place(x=370,y=290)
    
    bts=Button(t,text='Search',bd=1,font=1,bg='lavender',fg='blue',command=search)
    bts.place(x=680,y=155)
    
    bt=Button(t,text='Delete',bd=5,font=('Times New Roman',17),bg='light slate gray',fg='cyan',command=delete)
    bt.place(x=330,y=410)
    t.mainloop()
