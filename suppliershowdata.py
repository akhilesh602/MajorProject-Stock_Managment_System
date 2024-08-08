import tkinter
from tkinter import *
import pymysql
def suppshow():
    t=tkinter.Tk()
    t.title('show data')
    t.geometry('800x800')
    t.config(bg='dark khaki')
    
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
        sql="select * from supplier"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt1.append(res[0])
            lt2.append(res[1])
            lt3.append(res[2])
            lt4.append(res[3])
            lt5.append(res[4])
            lt6.append(res[5])
        db.close()
        
    def first():
        global i
        i=0
        b1.config(text=' ')
        d1.config(text=' ')
        e1.config(text=' ')
        f1.config(text=' ')
        g1.config(text=' ')
        h1.config(text=' ')
        b1.config(text=lt1[i]) 
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
        f1.config(text=lt4[i])
        g1.config(text=lt5[i])
        h1.config(text=lt6[i])
        
    def Next():
        global i
        i=i+1
        b1.config(text=' ')
        d1.config(text=' ')
        e1.config(text=' ')
        f1.config(text=' ')
        g1.config(text=' ')
        h1.config(text=' ')
        b1.config(text=lt1[i]) 
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
        f1.config(text=lt4[i])
        g1.config(text=lt5[i])
        h1.config(text=lt6[i])
        
    def Prev():
        global i
        i=i-1
        b1.config(text=' ')
        d1.config(text=' ')
        e1.config(text=' ')
        f1.config(text=' ')
        g1.config(text=' ')
        h1.config(text=' ')
        b1.config(text=lt1[i]) 
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
        f1.config(text=lt4[i])
        g1.config(text=lt5[i])
        h1.config(text=lt6[i])
        
    def last():
        global i
        i=len(lt1)-1
        b1.config(text=' ')
        d1.config(text=' ')
        e1.config(text=' ')
        f1.config(text=' ')
        g1.config(text=' ')
        h1.config(text=' ')
        b1.config(text=lt1[i]) 
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
        f1.config(text=lt4[i])
        g1.config(text=lt5[i])
        h1.config(text=lt6[i])
        
    a=Label(t,text='Supplier Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='dark khaki')
    a.place(x=280,y=30)
    
    b=Label(t,text='Supplier id',font=('Monotype Corsiva',26),bg='dark khaki')
    b.place(x=150,y=150)
    b1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='dark khaki',bd=4)
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
    
    bt1=Button(t,text='First',bd=3,bg='DarkSlategray3',font=1,fg='blue',command=first)
    bt1.place(x=150,y=600)
    
    bt2=Button(t,text='Next',bd=3,bg='DarkSlategray3',font=1,fg='blue',command=Next)
    bt2.place(x=300,y=600)
    
    bt3=Button(t,text='Previous',bd=3,bg='DarkSlategray3',font=1,fg='blue',command=Prev)
    bt3.place(x=475,y=600)
    
    bt4=Button(t,text='Last',bd=3,bg='DarkSlategray3',font=1,fg='blue',command=last)
    bt4.place(x=650,y=600)
    filldata()
    
    t.mainloop()
