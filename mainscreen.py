

import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

from companydelete import *
from companyinsert import *
from companyfind import *
from companyupdate import *
from companyshowdata import *

from billdelete import *
from billupdate import *
from billinsert import *
from billfind import *
from billshowdata import *

from categorydelete import *
from categoryinsert import *
from categoryupdate import *
from categoryfind import *
from categoryshowdata import *

from itemsdelete import *
from itemsinsert import *
from itemsupdate import *
from itemsfind import *
from itemsshowdata import *

from ordersprojectdelete import *
from ordersprojectupdate import *
from ordersprojectinsert import *
from ordersprojectfind import *
from ordersprojectshowdata import *
 
from stockdelete import *
from stockinsert import *
from stockupdate import *
from stockfind import *
from stockshowdata import *

from supplierdelete import *
from supplierinsert import *
from supplierupdate import *
from supplierfind import *
from suppliershowdata import *

from customerdelete import *
from customerinsert import *
from customerupdate import *
from customerfind import *
from customershowdata import *

def mainscreen():

    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Main Screen')
    t.config(bg='wheat3')
    a=Label(t,text='Main Screen',fg='firebrick2',bg='wheat3',font=('Monotype Corsiva',28,UNDERLINE))
    a.place(x=330,y=20)
    
    b=Label(t,text='Company',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',18))
    b.place(x=30,y=125)
    b1=Button(t,text='Insert',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=compinsert)
    b1.place(x=180,y=120)
    b2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=compfind)
    b2.place(x=300,y=120)
    b3=Button(t,text='Delete',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=compdelete)
    b3.place(x=420,y=120)
    b4=Button(t,text='Update',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=compupdate)
    b4.place(x=540,y=120)
    b5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=compshow)
    b5.place(x=680,y=120)
    
    
    d=Label(t,text='Category',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',18))
    d.place(x=30,y=205)
    d1=Button(t,text='Insert',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=catinsert)
    d1.place(x=180,y=200)
    d2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=catfind)
    d2.place(x=300,y=200)
    d3=Button(t,text='Delete',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=catdelete)
    d3.place(x=420,y=200)
    d4=Button(t,text='Update',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=catupdate)
    d4.place(x=540,y=200)
    d5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=catshow)
    d5.place(x=680,y=200)
    
    
    e=Label(t,text='Items',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',18))
    e.place(x=30,y=285)
    e1=Button(t,text='Insert',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=itemsinsert)
    e1.place(x=180,y=280)
    e2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=itemsfind)
    e2.place(x=300,y=280)
    e3=Button(t,text='Delete',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=itemsdelete)
    e3.place(x=420,y=280)
    e4=Button(t,text='Update',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=itemsupdate)
    e4.place(x=540,y=280)
    e5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=itemsshow)
    e5.place(x=680,y=280)
    
    
    f=Label(t,text='Supplier',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',18))
    f.place(x=30,y=365)
    f1=Button(t,text='Insert',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=suppinsert)
    f1.place(x=180,y=360)
    f2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=suppfind)
    f2.place(x=300,y=360)
    f3=Button(t,text='Delete',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=suppdelete)
    f3.place(x=420,y=360)
    f4=Button(t,text='Update',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=suppupdate)
    f4.place(x=540,y=360)
    f5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=suppshow)
    f5.place(x=680,y=360)
    
    
    g=Label(t,text='StockIn',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',18))
    g.place(x=30,y=445)
    g1=Button(t,text='Insert',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=stockinsert)
    g1.place(x=180,y=440)
    g2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=stockfind)
    g2.place(x=300,y=440)
    g3=Button(t,text='Delete',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=stockdelete)
    g3.place(x=420,y=440)
    g4=Button(t,text='Update',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=stockupdate)
    g4.place(x=540,y=440)
    g5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=stockshow)
    g5.place(x=680,y=440)
    
    
    h=Label(t,text='Customers',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',18))
    h.place(x=30,y=525)
    h1=Button(t,text='Insert',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=custinsert)
    h1.place(x=180,y=520)
    h2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=custfind)
    h2.place(x=300,y=520)
    h3=Button(t,text='Delete',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=custdelete)
    h3.place(x=420,y=520)
    h4=Button(t,text='Update',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=custupdate)
    h4.place(x=540,y=520)
    h5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=custshow)
    h5.place(x=680,y=520)
    
    
    j=Label(t,text='Orders',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',18))
    j.place(x=30,y=605)
    j1=Button(t,text='Insert',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=ordersinsert)
    j1.place(x=180,y=600)
    j2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=ordersfind)
    j2.place(x=300,y=600)
    j3=Button(t,text='Delete',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=ordersdelete)
    j3.place(x=420,y=600)
    j4=Button(t,text='Update',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=ordersupdate)
    j4.place(x=540,y=600)
    j5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=ordersshow)
    j5.place(x=680,y=600)
    
    
    k=Label(t,text='Bill',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',18))
    k.place(x=30,y=685)
    k1=Button(t,text='Insert',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=billinsert)
    k1.place(x=180,y=680)
    k2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=billfind)
    k2.place(x=300,y=680)
    k3=Button(t,text='Delete',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=billdelete)
    k3.place(x=420,y=680)
    k4=Button(t,text='Update',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=billupdate)
    k4.place(x=540,y=680)
    k5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=billshow)
    k5.place(x=680,y=680)
    
    t.mainloop()