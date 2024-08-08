

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

def userscreen():

    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Main Screen')
    t.resizable(width=False, height=False)
    d=Canvas(t,height=800,width=800,bg='pink')
    d.place(x=0,y=0)
    d.create_rectangle(70,100,710,760,outline='lavender',width=3,fill='LightPink3')
    d.create_rectangle(70,100,310,760,outline='lavender',width=3,fill='wheat3')
    
    
    
    a=Label(t,text='Main  Screen',fg='firebrick2',bg='pink',font=('Monotype Corsiva',34,UNDERLINE))
    a.place(x=330,y=20)

    b=Label(t,text='Company',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',20))
    b.place(x=90,y=125)

    b2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=compfind)
    b2.place(x=350,y=120)

    b5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=compshow)
    b5.place(x=580,y=120)


    d=Label(t,text='Category',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',20))
    d.place(x=90,y=205)
       
    d2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=catfind)
    d2.place(x=350,y=200)
       
    d5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=catshow)
    d5.place(x=580,y=200)


    e=Label(t,text='Items',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',20))
    e.place(x=90,y=285)
       
    e2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=itemsfind)
    e2.place(x=350,y=280)
       
    e5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=itemsshow)
    e5.place(x=580,y=280)


    f=Label(t,text='Supplier',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',20))
    f.place(x=90,y=365)
       
    f2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=suppfind)
    f2.place(x=350,y=360)

    f5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=suppshow)
    f5.place(x=580,y=360)


    g=Label(t,text='StockIn',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',20))
    g.place(x=90,y=445)

    g2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=stockfind)
    g2.place(x=350,y=440)

    g5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=stockshow)
    g5.place(x=580,y=440)


    h=Label(t,text='Customers',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',20))
    h.place(x=90,y=525)

    h2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=custfind)
    h2.place(x=350,y=520)
       
    h5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=custshow)
    h5.place(x=580,y=520)


    j=Label(t,text='Orders',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',20))
    j.place(x=90,y=605)

    j2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=ordersfind)
    j2.place(x=350,y=600)

    j5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=ordersshow)
    j5.place(x=580,y=600)


    k=Label(t,text='Bill',fg='royalblue4',bg='wheat3',font=('Arial Rounded MT Bold',20))
    k.place(x=90,y=685)

    k2=Button(t,text='Find',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=billfind)
    k2.place(x=350,y=680)

    k5=Button(t,text='Show',bd=2,bg='gray',font=('Times New Roman',17),fg='cyan',command=billshow)
    k5.place(x=580,y=680)

    t.mainloop()
