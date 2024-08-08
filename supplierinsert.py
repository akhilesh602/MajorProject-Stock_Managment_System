import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
import re
def suppinsert():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Supplier')
    t.config(bg='dark khaki')
   
    lt1=[]
    def fillcatid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select catid from supplier"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt1.append(res[0])
            
    lt2=[]
    def fillsuppid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select supplierid from supplier"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt2.append(res[0])
  
    def validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return True
        else:
            return False
        
    def searchid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        aa2=b1.get()
        ab=d1.get()
        sql="select count(0)  from supplier where supplierid='%s' "%(aa2)
        cur.execute(sql)
        data=cur.fetchone()
        b1.delete(0,100)
        if data[0]==0:
            messagebox.showinfo('Information','This id is not exits, you can insert it')
        else:
           messagebox.showerror('Information','This id is already exits please try with another one')
    
    def insert():
        if len(b1.get())==0 or len(d1.get())==0 or len(e1.get())==0 or len(f1.get())==0 or len(g1.get())==0 or len(h1.get())==0:
            messagebox.showinfo('hi','plss fill all data')
            
        elif len(g1.get())!=10:
            messagebox.showerror('Fill-up','Please insert 10 digit number')
            
        else:
            if validate_email(f1.get()):
                db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
                cur=db.cursor()
                aa=b1.get()
                ab=d1.get()
                ac=e1.get()
                ad=f1.get()
                ae=g1.get()
                af=h1.get()
                sql="insert into supplier values('%s','%s','%s','%s','%s','%s')"%(aa,ab,ac,ad,ae,af)
                cur.execute(sql)
                db.commit()
                b1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                h1.delete(0,100)
                db.close()
                messagebox.showinfo('Insert','Data is inserted in supplier')
            else:
                messagebox.showerror('hi','Invalid Email Id')
    def close():
        t.destroy()
        
    a=Label(t,text='Supplier Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='dark khaki')
    a.place(x=280,y=30)
    
    b=Label(t,text='Supplier id',font=('Monotype Corsiva',26),bg='dark khaki')
    b.place(x=120,y=150)
    b1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillsuppid()
    b1['values']=lt2
    b1.place(x=350,y=160)
    
    d=Label(t,text='Supplier name',font=('Monotype Corsiva',26),bg='dark khaki')
    d.place(x=120,y=220)
    d1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    d1.place(x=350,y=230)
    
    e=Label(t,text='Address',font=('Monotype Corsiva',26),bg='dark khaki')
    e.place(x=120,y=290)
    e1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    e1.place(x=350,y=300)
    
    f=Label(t,text='Email',font=('Monotype Corsiva',26),bg='dark khaki')
    f.place(x=120,y=370)
    f1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    f1.place(x=350,y=380)
    
    g=Label(t,text='Contact Info',font=('Monotype Corsiva',26),bg='dark khaki')
    g.place(x=120,y=440)
    g1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold"),fg='royalblue',bg='peachpuff',bd=4)
    g1.place(x=350,y=450)
    
    h=Label(t,text='Category id',font=('Monotype Corsiva',26),bg='dark khaki')
    h.place(x=120,y=500)
    h1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillcatid()
    h1['values']=lt1
    h1.place(x=350,y=505)
    
    bt=Button(t,text='Insert',bd=5,font=1,bg='DarkSlateGray3',fg='blue',command=insert)
    bt.place(x=280,y=650)
    
    bts=Button(t,text='Search',bd=1,font=1,bg='lavender',fg='blue',command=searchid)
    bts.place(x=700,y=158)
    
    btc=Button(t,text='Close',bd=5,font=1,bg='DarkSlateGray3',fg='blue',command=close)
    btc.place(x=370,y=650)

    t.mainloop()

