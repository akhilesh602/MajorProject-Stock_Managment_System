import tkinter
from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
def billupdate():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Bill')
    t.config(bg='aquamarine2')
    
    
    
    lt1=[]
    def fillbillid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select billid from bill"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt1.append(res[0])
            
    lt2=[]
    def fillorderid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select orderid from bill"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt2.append(res[0])
            
    lt3=[]
    def fillcustid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select custid from bill"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt3.append(res[0])
            
    lt4=[]
    def fillitemid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select itemid from bill"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt4.append(res[0])
            
            
    def update():
        if len(b1.get())==0 or len(d1.get())==0 or len(e1.get())==0 or len(f1.get())==0 or len(g1.get())==0:
            messagebox.showinfo('hi','plss fill all data')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa3=b1.get()
            ab3=d1.get()
            ad3=e1.get()
            ae3=f1.get()
            af3=int(g1.get())
            sql3="update bill set orderid='%s', custid='%s', itemid='%s', amount='%d' where billid='%s'"%(ab3,ad3,ae3,af3,aa3)
            cur.execute(sql3)
            db.commit()
            db.close()
            messagebox.showinfo('Update','Data Updated')
        
        
    a=Label(t,text='Bill Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='aquamarine2')
    a.place(x=330,y=30)
    
    b=Label(t,text='Bill id',font=('Monotype Corsiva',26),bg='aquamarine2')
    b.place(x=130,y=150)
    b1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='peachpuff',background='peachpuff')
    fillbillid()
    b1['values']=lt1
    b1.place(x=330,y=160)
    
    d=Label(t,text='Order id',font=('Monotype Corsiva',26),bg='aquamarine2')
    d.place(x=130,y=220)
    d1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='peachpuff',background='peachpuff')
    fillorderid()
    d1['values']=lt2
    d1.place(x=330,y=230)
    
    e=Label(t,text='Customer id',font=('Monotype Corsiva',26),bg='aquamarine2')
    e.place(x=130,y=280)
    e1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='peachpuff',background='peachpuff')
    fillcustid()
    e1['values']=lt3
    e1.place(x=330,y=290)
    
    f=Label(t,text='Item id',font=('Monotype Corsiva',26),bg='aquamarine2')
    f.place(x=130,y=340)
    f1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='peachpuff',background='peachpuff')
    fillitemid()
    f1['values']=lt4
    f1.place(x=330,y=350)
    
    g=Label(t,text='Amount',font=('Monotype Corsiva',26),bg='aquamarine2')
    g.place(x=130,y=400)
    g1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    g1.place(x=330,y=410)
    
    bt=Button(t,text='Update',bd=7,font=1,bg='khaki1',fg='blue',command=update)
    bt.place(x=330,y=520)
    
   
    t.mainloop()
