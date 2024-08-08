import tkinter
from tkinter import *
from logindetails import *
from admin import *

t=tkinter.Tk()
t.geometry('800x800')
t.title('Login')

t.resizable(width=False, height=False)
d=Canvas(t,height=800,width=800,bg='gray20')
d.place(x=0,y=0)
d1=Canvas(t,height=245,width=800,bg='gray24')
d1.place(x=0,y=0)

d.create_line(0,250,800,250,width=5,fill='gray28')


d.create_rectangle(250,330,545,750,outline='lavender',width=3,fill='gray38')
d.create_line(545,390,545,750,width=3,fill='royalblue')
d.create_line(320,750,545,750,width=3,fill='royalblue')
d.create_line(250,330,485,330,width=3,fill='royalblue')
d.create_line(250,330,250,690,width=3,fill='royalblue')


a=Label(t,text=' Welcome ',fg='red',font=('Lucida Calligraphy',25),bg='gray24')
a.place(x=300,y=30)

b=Label(t,text=' to ',fg='red',font=('Lucida Calligraphy',25),bg='gray24')
b.place(x=360,y=100)

c=Label(t,text='Stock Managment System',fg='red',font=('Lucida Calligraphy',25,UNDERLINE),bg='gray24')
c.place(x=150,y=180)
 
d=Label(t,text='Login  as  Admin ',font=('Arial Rounded MT Bold',22),fg='lavender',bg='gray38')
d.place(x=280,y=370)
d1=Button(t,text='Admin',bd=7,width=10,font=1,bg='gray24',fg='cyan',command=admin)
d1.place(x=330,y=465)
 
e=Label(t,text='Login  as  User',font=('Arial Rounded MT Bold',22),fg='lavender',bg='gray38')
e.place(x=285,y=560)
e1=Button(t,text='User',bd=7,width=10,font=1,bg='gray24',fg='cyan',command=user)
e1.place(x=330,y=640)
t.mainloop()