import tkinter
from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
def catupdate():
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
            
            
    def update():
        if len(b1.get())==0 or len(d1.get())==0 or len(e1.get())==0:
            messagebox.showinfo('hi','plss fill all data')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa3=b1.get()
            ab3=d1.get()
            ad3=e1.get()
            sql3="update category set catname='%s', description='%s' where catid='%s'"%(ab3,ad3,aa3)
            cur.execute(sql3)
            db.commit()
            db.close()
            messagebox.showinfo('Update','Data Updated')
        
        
    a=Label(t,text='Category Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='thistle3')
    a.place(x=280,y=30)
    
    b=Label(t,text='Category id',font=('Monotype Corsiva',26),bg='thistle3')
    b.place(x=100,y=150)
    b1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine',background='peachpuff')
    fillcatid()
    b1['values']=lt
    b1.place(x=330,y=160)
    
    d=Label(t,text='Category Name',font=('Monotype Corsiva',26),bg='thistle3')
    d.place(x=100,y=220)
    d1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    d1.place(x=330,y=230)
    
    e=Label(t,text='Description',font=('Monotype Corsiva',26),bg='thistle3')
    e.place(x=100,y=280)
    e1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    e1.place(x=330,y=290)
    
    bt=Button(t,text='Update',bd=5,font=('Times New Roman',17),bg='light slate gray',fg='cyan',command=update)
    bt.place(x=330,y=410)
    t.mainloop()
