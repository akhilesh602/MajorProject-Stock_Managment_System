import tkinter
from tkinter import *
import pymysql
def custshow():
    t=tkinter.Tk()
    t.title('show data')
    t.geometry('800x800')
    t.config(bg='plum3')
    
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
        sql="select * from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt1.append(res[0])
            lt2.append(res[1])
            lt3.append(res[2])
            lt4.append(res[3])
          
        db.close()
        
    def first():
        global i
        i=0
        b1.config(text=' ')
        d1.config(text=' ')
        e1.config(text=' ')
        f1.config(text=' ')
        b1.config(text=lt1[i]) 
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
        f1.config(text=lt4[i])
    
        
    def Next():
        global i
        i=i+1
        b1.config(text=' ')
        d1.config(text=' ')
        e1.config(text=' ')
        f1.config(text=' ')
        b1.config(text=lt1[i]) 
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
        f1.config(text=lt4[i])
     
        
    def Prev():
        global i
        i=i-1
        b1.config(text=' ')
        d1.config(text=' ')
        e1.config(text=' ')
        f1.config(text=' ')
        b1.config(text=lt1[i]) 
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
        f1.config(text=lt4[i])
       
        
    def last():
        global i
        i=len(lt1)-1
        b1.config(text=' ')
        d1.config(text=' ')
        e1.config(text=' ')
        f1.config(text=' ')
        b1.config(text=lt1[i]) 
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
        f1.config(text=lt4[i])
        
      
        
    a=Label(t,text='Customer Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='plum3')
    a.place(x=280,y=30)
    
    b=Label(t,text='Customer id',font=('Monotype Corsiva',26),bg='plum3')
    b.place(x=150,y=150)
    b1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='plum3',bd=4)
    b1.place(x=350,y=155)
    
    d=Label(t,text='Customer Name',font=('Monotype Corsiva',26),bg='plum3')
    d.place(x=150,y=220)
    d1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='plum3',bd=4)
    d1.place(x=350,y=220)
    
    e=Label(t,text='Contact no.',font=('Monotype Corsiva',26),bg='plum3')
    e.place(x=150,y=290)
    e1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='plum3',bd=4)
    e1.place(x=350,y=290)
    
    f=Label(t,text='Email',font=('Monotype Corsiva',26),bg='plum3')
    f.place(x=150,y=360)
    f1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='plum3',bd=4)
    f1.place(x=350,y=360)
    
    bt1=Button(t,text='First',bd=3,bg='DarkSlateGray3',font=1,fg='blue',command=first)
    bt1.place(x=150,y=450)
    
    bt2=Button(t,text='Next',bd=3,bg='DarkSlateGray3',font=1,fg='blue',command=Next)
    bt2.place(x=300,y=450)
    
    bt3=Button(t,text='Previous',bd=3,bg='DarkSlateGray3',font=1,fg='blue',command=Prev)
    bt3.place(x=475,y=450)
    
    bt4=Button(t,text='Last',bd=3,bg='DarkSlateGray3',font=1,fg='blue',command=last)
    bt4.place(x=650,y=450)
    filldata()
    
    t.mainloop()
