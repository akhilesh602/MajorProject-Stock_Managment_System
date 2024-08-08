import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def billfind():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Bill')
    t.config(bg='aquamarine2')
    
    lt=[]
    def fillbillid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select billid from bill"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
    
    def find():
        if len(b1.get())==0:
            messagebox.showinfo('hi','plss fill billid')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa1=b1.get()
            sql1="select * from bill where billid='%s'"%(aa1)
            cur.execute(sql1)
            data=cur.fetchone()
            d1.config(text=' ')
            e1.config(text=' ')
            f1.config(text=' ')
            g1.config(text=' ')
            d1.config(text=data[1])
            e1.config(text=data[2])
            f1.config(text=data[3])
            g1.config(text=data[4])
            db.close()
            messagebox.showinfo('Find','Data Found')
        
        
    a=Label(t,text='Bill Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='aquamarine2')
    a.place(x=330,y=30)
    
    b=Label(t,text='Bill id',font=('Monotype Corsiva',26),bg='aquamarine2')
    b.place(x=200,y=150)
    b1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='peachpuff',background='peachpuff')
    fillbillid()
    b1['values']=lt
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
    
    bt=Button(t,text='Find',bd=7,font=1,bg='khaki1',fg='blue',command=find)
    bt.place(x=330,y=520)
    
   
    t.mainloop()

