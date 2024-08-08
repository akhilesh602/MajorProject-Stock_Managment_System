import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def forgotid():
    t=tkinter.Tk()
    t.title('Forgot Password')
    t.geometry('600x200')
    t.config(bg='pink3')
    
    def ok():
        
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            x=a1.get()
            sql="select * from usertable where email='%s'"%(x)
            cur.execute(sql)
            data=cur.fetchone()
            from_address = "akhileshsisodia.602@gmail.com"
            to_address = (a1.get())
        
        
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Login Details"
            msg['From'] = from_address
            msg['To'] = to_address
        
        
            
            html = 'user id is      '+data[4]+ '    and password is     '+data[5]
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
            messagebox.showinfo('Send','We have send you an email with your userid and password')
            a1.delete(0,100)
            db.close()
    
    
    a=Label(t,text='Enter Your Registrate email',font=('Arial Rounded MT Bold',14),bg='pink3')
    a.place(x=10,y=60)
    a1=Entry(t,width=40,fg='royalblue',bd=3)
    a1.place(x=280,y=65)
    bt=Button(t,text='   ok   ',bg='khaki',fg='blue',bd=3,font=2,command=ok)
    bt.place(x=250,y=120)
    t.mainloop()


