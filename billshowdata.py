import tkinter
from tkinter import *
import pymysql
def billshow():
    t=tkinter.Tk()
    t.title('show data')
    t.geometry('800x800')
    t.config(bg='aquamarine2')
    
    lt1=[]
    lt2=[]
    lt3=[]
    lt4=[]
    lt5=[]
    
    i=0
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select * from bill"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt1.append(res[0])
            lt2.append(res[1])
            lt3.append(res[2])
            lt4.append(res[3])
            lt5.append(res[4])
            
        db.close()
        
    def first():
        global i
        i=0
        d1.config(text=' ')
        e1.config(text=' ')
        f1.config(text=' ')
        g1.config(text=' ')
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
        f1.config(text=lt4[i])
        g1.config(text=lt5[i])
        b1.config(text=lt1[i])
        
        
    def Next():
        global i
        i=i+1
        d1.config(text=' ')
        e1.config(text=' ')
        f1.config(text=' ')
        g1.config(text=' ')
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
        f1.config(text=lt4[i])
        g1.config(text=lt5[i])
        b1.config(text=lt1[i])
        
        
    def Prev():
        global i
        i=i-1
        d1.config(text=' ')
        e1.config(text=' ')
        f1.config(text=' ')
        g1.config(text=' ')
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
        f1.config(text=lt4[i])
        g1.config(text=lt5[i])
        b1.config(text=lt1[i])
        
    def last():
        global i
        i=len(lt1)-1
        d1.config(text=' ')
        e1.config(text=' ')
        f1.config(text=' ')
        g1.config(text=' ')
        d1.config(text=lt2[i])
        e1.config(text=lt3[i])
        f1.config(text=lt4[i])
        g1.config(text=lt5[i])
        b1.config(text=lt1[i])
        
        
    a=Label(t,text='Bill Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='aquamarine2')
    a.place(x=330,y=30)
    
    b=Label(t,text='Bill id',font=('Monotype Corsiva',26),bg='aquamarine2')
    b.place(x=200,y=150)
    b1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='aquamarine2',bd=4)
    b1.place(x=320,y=160)
    
    d=Label(t,text='Order id',font=('Monotype Corsiva',26),bg='aquamarine2')
    d.place(x=200,y=220)
    d1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='aquamarine2',bd=4)
    d1.place(x=320,y=230)
    
    e=Label(t,text='Customer id',font=('Monotype Corsiva',26),bg='aquamarine2')
    e.place(x=200,y=280)
    e1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='aquamarine2',bd=4)
    e1.place(x=320,y=290)
    
    f=Label(t,text='Item id',font=('Monotype Corsiva',26),bg='aquamarine2')
    f.place(x=200,y=340)
    f1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='aquamarine2',bd=4)
    f1.place(x=320,y=350)
    
    g=Label(t,text='Amount',font=('Monotype Corsiva',26),bg='aquamarine2')
    g.place(x=200,y=400)
    g1=Label(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='aquamarine2',bd=4)
    g1.place(x=320,y=410)
    
    
    bt1=Button(t,text='First',bd=7,bg='khaki1',font=1,fg='blue',command=first)
    bt1.place(x=150,y=500)
    
    bt2=Button(t,text='Next',bd=7,bg='khaki1',font=1,fg='blue',command=Next)
    bt2.place(x=300,y=500)
    
    bt3=Button(t,text='Previous',bd=7,bg='khaki1',font=1,fg='blue',command=Prev)
    bt3.place(x=475,y=500)
    
    bt4=Button(t,text='Last',bd=7,bg='khaki1',font=1,fg='blue',command=last)
    bt4.place(x=650,y=500)
    filldata()
    
    t.mainloop()
