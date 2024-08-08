import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
import math
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkcalendar import DateEntry

def ordersinsert():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Orders')
    t.config(bg='LavenderBlush3')
    
    def get_date():
        selected_date = cal.get()
        h1.insert(0,selected_date)
        
    lt1=[]
    def fillorderid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select orderid from orders"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt1.append(res[0])
            
    lt2=[]
    def fillcustid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select custid from orders"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt2.append(res[0])
            
    lt3=[]
    def fillitemid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select itemid from orders"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt3.append(res[0])
            
    lt4=[]
    def fillcatid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select catid from orders"
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
        sql="select count(0)  from orders where orderid='%s' "%(aa2)
        cur.execute(sql)
        data=cur.fetchone()
        b1.delete(0,100)
        if data[0]==0:
            messagebox.showinfo('Information','This id is not exits, you can insert it')
        else:
           messagebox.showerror('Information','This id is already exits please try with another one')
    def updateitems():
        x=e1.get()
        y=int(g1.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="update items set currqty=currqty-'%d' where itemid='%s'"%(y,x)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','Stock Update')
        db.close()
    
        
    def sendorders(cid,u,v,x,y,z):
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select email from customers where custid='%s'"%(cid)
        cur.execute(sql)
        data=cur.fetchone()
        em=data[0]
        
        from_address = "akhileshsisodia.602@gmail.com"
        to_address = em
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Order data"
        msg['From'] = from_address
        msg['To'] = to_address
        
        html="Thanks \n"+cid+"Customer Id"+u+"\nOrder id"+v+"\nItem Id"+x+"\nCategory Id"+y+"\nQuantity"+z+"\nDate of Order"
        
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
        if len(b1.get())==0 or len(d1.get())==0 or len(e1.get())==0 or len(f1.get())==0 or len(g1.get())==0 or len(h1.get())==0:
            messagebox.showinfo('hi','plss fill all data')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa=b1.get()
            ab=d1.get()
            ac=e1.get()
            ad=f1.get()
            ae=int(g1.get())
            af=h1.get()
            sql="insert into orders values('%s','%s','%s','%s','%d','%s')"%(aa,ab,ac,ad,ae,af)
            cur.execute(sql)
            db.commit()
            updateitems()
            sendorders(ab,aa,ac,ad,str(ae),af)
            b1.delete(0,100)
            d1.delete(0,100)
            e1.delete(0,100)
            f1.delete(0,100)
            g1.delete(0,100)
            h1.delete(0,100)
            db.close()
            messagebox.showinfo('Insert','Data is inserted in orders')
        
    a=Label(t,text='Orders Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='LavenderBlush3')
    a.place(x=280,y=30)
    
    b=Label(t,text='Order id',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    b.place(x=120,y=150)
    b1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillorderid()
    b1['values']=lt1
    b1.place(x=350,y=160)
    
    d=Label(t,text='Customerid id',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    d.place(x=120,y=220)
    d1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillcustid()
    d1['values']=lt2
    d1.place(x=350,y=230)
    
    e=Label(t,text='Item id',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    e.place(x=120,y=290)
    e1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillitemid()
    e1['values']=lt3
    e1.place(x=350,y=300)
    
    f=Label(t,text='Category id',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    f.place(x=120,y=370)
    f1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='lavender',background='peachpuff')
    fillcatid()
    f1['values']=lt4
    f1.place(x=350,y=380)
    
    g=Label(t,text='Quantity',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    g.place(x=120,y=440)
    g1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    g1.place(x=350,y=450)
    
    h=Label(t,text='Date of Order',font=('Monotype Corsiva',26),bg='LavenderBlush3')
    h.place(x=120,y=520)
    h1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    h1.place(x=350,y=530)
    
    cal = DateEntry(t, date_pattern="yyyy-mm-dd",width=13,bd=5)
    cal.place(x=680,y=530)
    
    bt=Button(t,text='Insert',bd=5,font=1,bg='light slate gray',fg='spring green',command=insert)
    bt.place(x=330,y=650)
    
    bts=Button(t,text='Search',bd=1,font=1,bg='lavender',fg='blue',command=searchid)
    bts.place(x=700,y=158)
    
    bts1=Button(t,text='Date',bd=1,font=1,bg='lavender',fg='blue',command=get_date)
    bts1.place(x=700,y=558)
    t.mainloop()

