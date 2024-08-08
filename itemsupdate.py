import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def itemsupdate():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Items')
    t.config(bg='MistyRose2')
    
    lt1=[]
    def fillitemid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select itemid from items"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt1.append(res[0])
    
    lt2=[]
    def fillcatid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select catid from items"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt2.append(res[0])
    def update():
        if len(b1.get())==0 or len(d1.get())==0 or len(e1.get())==0 or len(f1.get())==0 or len(g1.get())==0 or len(h1.get()) or len(j1.get())==0:
            messagebox.showinfo('hi','plss fill all data')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa3=b1.get()
            ab3=d1.get()
            ad3=e1.get()
            ae3=int(f1.get())
            af3=int(g1.get())
            ag3=int(h1.get())
            ah3=int(j1.get())
            sql3="update items set catid='%s', iname='%s', unit='%d', price='%d', openqty='%d', currqty='%d' where itemid='%s'"%(ab3,ad3,ae3,af3,ag3,ah3,aa3)
            cur.execute(sql3)
            db.commit()
            db.close()
            messagebox.showinfo('Update','Data Updated')
    
        
    a=Label(t,text='Items Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='MistyRose2')
    a.place(x=280,y=30)
    
    b=Label(t,text='Item id',font=('Monotype Corsiva',26),bg='MistyRose2')
    b.place(x=120,y=150)
    b1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillitemid()
    b1['values']=lt1
    b1.place(x=350,y=160)
    
    d=Label(t,text='Category id',font=('Monotype Corsiva',26),bg='MistyRose2')
    d.place(x=120,y=220)
    d1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillcatid()
    d1['values']=lt2
    d1.place(x=350,y=230)
    
    e=Label(t,text='Item name',font=('Monotype Corsiva',26),bg='MistyRose2')
    e.place(x=120,y=290)
    e1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='aquamarine2',bd=4)
    e1.place(x=350,y=300)
    
    f=Label(t,text='Unit',font=('Monotype Corsiva',26),bg='MistyRose2')
    f.place(x=120,y=370)
    f1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='aquamarine2',bd=4)
    f1.place(x=350,y=380)
    
    g=Label(t,text='Price',font=('Monotype Corsiva',26),bg='MistyRose2')
    g.place(x=120,y=440)
    g1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='aquamarine2',bd=4)
    g1.place(x=350,y=450)
    
    h=Label(t,text='Open Quantity',font=('Monotype Corsiva',26),bg='MistyRose2')
    h.place(x=120,y=520)
    h1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='aquamarine2',bd=4)
    h1.place(x=350,y=530)
    
    j=Label(t,text='Current Quantity',font=('Monotype Corsiva',26),bg='MistyRose2')
    j.place(x=120,y=600)
    j1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='aquamarine2',bd=4)
    j1.place(x=350,y=610)
    
    
    
    
    bt=Button(t,text='Update',bd=5,font=1,bg='dim gray',fg='cyan',command=update)
    bt.place(x=330,y=680)
    t.mainloop()
