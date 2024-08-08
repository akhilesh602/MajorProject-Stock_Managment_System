import tkinter
from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
import math
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def billinsert():
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
    def searchid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        aa2=b1.get()
        ab=d1.get()
        sql="select count(0)  from bill where billid='%s' "%(aa2)
        cur.execute(sql)
        data=cur.fetchone()
        b1.delete(0,100)
        if data[0]==0:
            messagebox.showinfo('Information','This id is not exits, you can insert it')
        else:
           messagebox.showerror('Information','This id is already exits please try with another one')
            
           
    def updatestock():
        x=d1.get()
        y=int(h1.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="update items set currqty=currqty-%d where itemid='%s'"%(y,x)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','Stock Update')
        db.close()
    
        
    def sendbill(cid,u,v,x,y):
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select email from customers where custid='%s'"%(cid)
        cur.execute(sql)
        data=cur.fetchone()
        em=data[0]
        
        from_address = "akhileshsisodia.602@gmail.com"
        to_address = em
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Bill data"
        msg['From'] = from_address
        msg['To'] = to_address
        
        html="Thanks \n"+cid+"Customer Id"+u+"\nBill id"+v+"\nOrder Id"+x+"\nItem Id"+y+"\nAmount"
        
        part1 = MIMEText(html, 'html')
        msg.attach(part1)
        username = 'akhileshsisodia.602@gmail.com' 
        password = 'eybwrfajrwrhzkqy'
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.login(username,password)  
        server.sendmail(from_address, to_address, msg.as_string())  
        server.quit()
        messagebox.showinfo('Alert','Mail sent')
        
    def insert():
        if len(b1.get())==0 or len(d1.get())==0 or len(e1.get())==0 or len(f1.get())==0 or len(g1.get())==0:
            messagebox.showinfo('hi','plss fill all data')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa=b1.get()
            ab=d1.get()
            ac=e1.get()
            ad=f1.get()
            ae=int(g1.get())
            sql="insert into bill values('%s','%s','%s','%s','%d')"%(aa,ab,ac,ad,ae)
            cur.execute(sql)
            db.commit()
            
            sendbill(ac,aa,ab,ad,str(ae))
            b1.delete(0,100)
            d1.delete(0,100)
            e1.delete(0,100)
            f1.delete(0,100)
            g1.delete(0,100)
            db.close()
            messagebox.showinfo('Insert','Data is inserted in Bill')
        
    
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
    
    bt=Button(t,text='Insert',bd=7,font=1,bg='khaki1',fg='blue',command=insert)
    bt.place(x=330,y=520)
    
    bts=Button(t,text='Search',bd=1,font=1,bg='lavender',fg='blue',command=searchid)
    bts.place(x=680,y=155)
    t.mainloop()
