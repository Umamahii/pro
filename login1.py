import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call

def Ok():
    mysqldb = mysql.connector.connect(host="localhost",user="root",password="",database="College")
    mycursor = mysqldb.cursor()
    uname = e1.get()
    password = e2.get()


    sql = "select * from login where uname = %s and password = *s"
    mycursor.execute(sql, [(uname),(password)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("","Login Success")
        root.destroy()
        call(["python","main.py"])
        return True
    else:
        messagebox.showinfo("","Incorrent Username and Password")
        return False
root = Tk()
root.title("Login")
root.geometry("300x200")
global e1
global e2
Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)
e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")
Button(root, text="Login", command=Ok ,height = 3, width = 13).place(x=10, y=100)
root.mainloop()


