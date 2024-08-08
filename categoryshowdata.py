import tkinter
from tkinter import *
from tkinter import ttk
import pymysql
def catshow():
    t=tkinter.Tk()
    t.title('show data')
    t.geometry('800x800')
    t.config(bg='thistle3')
    
    lt1=[]
    lt2=[]
    lt3=[]
    lt4=[]
    lt5=[]
    lt6=[]
    i=0
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select * from category"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt1.append(res[0])
            lt2.append(res[1])
            lt3.append(res[2])
           
        db.close()
        
    def first():
        global i
        i=0
        b1.config(text=' ')
        d1.config(text=' ')
        e1.config(text=' ')
        b1.config(text=lt1[i])
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
     
        
    def Next():
        global i
        i=i+1
        b1.config(text=' ')
        d1.config(text=' ')
        e1.config(text=' ')
        b1.config(text=lt1[i])
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
    
        
    def Prev():
        global i
        i=i-1
        b1.config(text=' ')
        d1.config(text=' ')
        e1.config(text=' ')
        b1.config(text=lt1[i])
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
       
        
    def last():
        global i
        i=len(lt1)-1
        b1.config(text=' ')
        d1.config(text=' ')
        e1.config(text=' ')
        b1.config(text=lt1[i])
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
       
        
    a=Label(t,text='Category Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='thistle3')
    a.place(x=270,y=30)
    
    b=Label(t,text='Category id',font=('Monotype Corsiva',26),bg='thistle3')
    b.place(x=180,y=150)
    b1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='thistle3',bd=4)
    b1.place(x=370,y=160)
    
    d=Label(t,text='Category name',font=('Monotype Corsiva',26),bg='thistle3')
    d.place(x=180,y=250)
    d1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='thistle3',bd=4)
    d1.place(x=370,y=260)
    
    e=Label(t,text='Description',font=('Monotype Corsiva',26),bg='thistle3')
    e.place(x=180,y=350)
    e1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='thistle3',bd=4)
    e1.place(x=370,y=360)
    
    
    bt1=Button(t,text='First',bd=5,font=('Times New Roman',17),bg='light slate gray',fg='cyan',command=first)
    bt1.place(x=150,y=500)
    
    bt2=Button(t,text='Next',bd=5,font=('Times New Roman',17),bg='light slate gray',fg='cyan',command=Next)
    bt2.place(x=300,y=500)
    
    bt3=Button(t,text='Previous',bd=5,font=('Times New Roman',17),bg='light slate gray',fg='cyan',command=Prev)
    bt3.place(x=475,y=500)
    
    bt4=Button(t,text='Last',bd=5,font=('Times New Roman',17),bg='light slate gray',fg='cyan',command=last)
    bt4.place(x=650,y=500)
    filldata()
    
    t.mainloop()
