import tkinter
from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
def stockdelete():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('StockIn')
    t.config(bg='DarkSeaGreen1')
    
    lt=[]
    def fillstockinid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select stockinid from stockin"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
    
    def delete():
        if len(b1.get())==0:
            messagebox.showinfo('hi','plss Stockin id')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa2=b1.get()
            sql2="delete from stockin where stockinid='%s'"%(aa2)
            cur.execute(sql2)
            db.commit()
            db.close()
            messagebox.showinfo('Delete','Data Deleted')
            
    def Search():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        aa1=b1.get()
        sql1="select * from stockin where stockinid='%s'"%(aa1)
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
        
        
    a=Label(t,text='Stockin Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='DarkSeaGreen1')
    a.place(x=280,y=30)
    
    b=Label(t,text='Stockin id',font=('Monotype Corsiva',26),bg='DarkSeaGreen1')
    b.place(x=150,y=150)
    b1=ttk.Combobox(t,width=10,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillstockinid()
    b1['values']=lt
    b1.place(x=440,y=160)
    
    d=Label(t,text='Item id',font=('Monotype Corsiva',26),bg='DarkSeaGreen1')
    d.place(x=150,y=220)
    d1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='DarkSeaGreen1',bd=4)
    d1.place(x=350,y=225)
    
    e=Label(t,text='Category id',font=('Monotype Corsiva',26),bg='DarkSeaGreen1')
    e.place(x=150,y=290)
    e1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='DarkSeaGreen1',bd=4)
    e1.place(x=350,y=295)
    
    f=Label(t,text='Supplier',font=('Monotype Corsiva',26),bg='DarkSeaGreen1')
    f.place(x=150,y=360)
    f1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='DarkSeaGreen1',bd=4)
    f1.place(x=350,y=365)
    
    g=Label(t,text='Date In',font=('Monotype Corsiva',26),bg='DarkSeaGreen1')
    g.place(x=150,y=430)
    g1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='DarkSeaGreen1',bd=4)
    g1.place(x=350,y=435)
    
    h=Label(t,text='Quantity',font=('Monotype Corsiva',26),bg='DarkSeaGreen1')
    h.place(x=150,y=500)
    h1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='DarkSeaGreen1',bd=4)
    h1.place(x=350,y=505)
    
    bt=Button(t,text='Delete',bd=5,font=1,bg='DarkSlateGray3',fg='blue',command=delete)
    bt.place(x=330,y=620)
    
    bts=Button(t,text='Search',bd=1,font=1,bg='lavender',fg='blue',command=Search)
    bts.place(x=650,y=155)
    t.mainloop()


            
        
    