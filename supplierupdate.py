import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def suppupdate():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Supplier')
    t.config(bg='dark khaki')
    
    lt=[]
    lt1=[]
    def fillsupplierid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select supplierid from supplier"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        
    
    def fillcatid():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        sql="select catid from supplier"
        cur.execute(sql)
        data=cur.fetchall()
        for xyz in data:
            lt1.append(xyz[0])
            
            
    def update():
        if len(b1.get())==0 or len(d1.get())==0 or len(e1.get())==0 or len(f1.get())==0 or len(g1.get())==0 or len(h1.get())==0:
            messagebox.showinfo('hi','plss fill all data')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            aa3=b1.get()
            ab3=d1.get()
            ad3=e1.get()
            ae3=f1.get()
            af3=g1.get()
            ag3=h1.get()
            sql3="update supplier set sname='%s', address='%s', email='%s', phone='%s', catid='%s' where supplierid='%s'"%(ab3,ad3,ae3,af3,ag3,aa3)
            cur.execute(sql3)
            db.commit()
            db.close()
            messagebox.showinfo('Update','Data Updated')
        
        
    a=Label(t,text='Supplier Info',fg='firebrick2',font=('Lucida Calligraphy',28,UNDERLINE),bg='dark khaki')
    a.place(x=280,y=30)
    
    b=Label(t,text='Supplier id',font=('Monotype Corsiva',26),bg='dark khaki')
    b.place(x=120,y=150)
    b1=ttk.Combobox(t,width=25,font=("Comic Sans MS", 14,"bold") )
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillsupplierid()
    b1['values']=lt
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
    style1=ttk.Style()
    style1.theme_use('clam')
    style1.configure("TCombobox",fieldbackground='aquamarine2',background='peachpuff')
    fillcatid()
    h1['values']=lt1
    h1.place(x=350,y=505)
    
    bt=Button(t,text='Update',bd=5,font=1,bg='DarkSlateGray3',fg='blue',command=update)
    bt.place(x=330,y=650)
    

    t.mainloop()




