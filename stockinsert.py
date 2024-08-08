import tkinter
from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
def stockinsert():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('StockIn')
    t.config(bg='DarkSeaGreen1')
    
    lt1=[]
    def fillstockinid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select stockinid from stockin"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt1.append(res[0])
    lt2=[]
    def fillitemid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select itemid from stockin"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt2.append(res[0])
    lt3=[]
    def fillcatid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select catid from stockin"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt3.append(res[0])
    lt4=[]
    def fillsupplierid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select supplier from stockin"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt4.append(res[0])
            
            
    lt=[]
    def searchid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        aa2=b1.get()
        ab=d1.get()
        sql="select count(0)  from company where compid='%s' "%(aa2)
        cur.execute(sql)
        data=cur.fetchone()
        b1.delete(0,100)
        if data[0]==0:
            messagebox.showinfo('Information','This id is not exits, you can insert it')
        else:
           messagebox.showerror('Information','This id is already exits please try with another one')
    
    def updateitems():
        x=d1.get()
        y=int(h1.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="update items set currqty=currqty+'%d' where itemid='%s'"%(y,x)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','Stock Update')
        db.close()
    

        
        
    def insert():
        if len(b1.get())==0 or len(d1.get())==0 or len(e1.get())==0 or len(f1.get())==0 or len(g1.get())==0 or len(h1.get())==0:
            messagebox.showinfo('hi','plss fill all data')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa=b1.get()
            ab=d1.get()
            ac=e1.get()
            ad=f1.get()
            ae=g1.get()
            af=int(h1.get())
            sql="insert into stockin values('%s','%s','%s','%s','%s','%d')"%(aa,ab,ac,ad,ae,af)
            cur.execute(sql)
            db.commit()
            updateitems()
            b1.delete(0,100)
            d1.delete(0,100)
            e1.delete(0,100)
            f1.delete(0,100)
            g1.delete(0,100)
            h1.delete(0,100)
            db.close()
            messagebox.showinfo('Insert','Data is inserted in Stockin')
        
        
    a=Label(t,text='Stockin Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='DarkSeaGreen1')
    a.place(x=280,y=30)
    
    b=Label(t,text='Stockin id',font=('Monotype Corsiva',26),bg='DarkSeaGreen1')
    b.place(x=120,y=150)
    b1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillstockinid()
    b1['values']=lt1
    b1.place(x=350,y=160)
    
    d=Label(t,text='Item id',font=('Monotype Corsiva',26),bg='DarkSeaGreen1')
    d.place(x=120,y=220)
    d1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillitemid()
    d1['values']=lt2
    d1.place(x=350,y=230)
    
    e=Label(t,text='Category id',font=('Monotype Corsiva',26),bg='DarkSeaGreen1')
    e.place(x=120,y=290)
    e1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillcatid()
    e1['values']=lt3
    e1.place(x=350,y=300)
    
    f=Label(t,text='Supplier id',font=('Monotype Corsiva',26),bg='DarkSeaGreen1')
    f.place(x=120,y=370)
    f1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='MistyRose2',background='peachpuff')
    fillsupplierid()
    f1['values']=lt4
    f1.place(x=350,y=380)
    
    g=Label(t,text='Date In',font=('Monotype Corsiva',26),bg='DarkSeaGreen1')
    g.place(x=120,y=440)
    g1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    g1.place(x=350,y=450)
    
    h=Label(t,text='Quantity',font=('Monotype Corsiva',26),bg='DarkSeaGreen1')
    h.place(x=120,y=520)
    h1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    h1.place(x=350,y=530)
    
    bt=Button(t,text='Insert',bd=5,font=1,bg='DarkSlateGray3',fg='blue',command=insert)
    bt.place(x=330,y=650)
    
    bts=Button(t,text='Search',bd=1,font=1,bg='lavender',fg='blue',command=searchid)
    bts.place(x=700,y=158)
    t.mainloop()


