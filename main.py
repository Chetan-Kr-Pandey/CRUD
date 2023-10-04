import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['Student ID'])
    e2.insert(0,select['Student Name'])
    e3.insert(0,select['Contribution(Rs)'])
    e4.insert(0,select['Work_done'])
    e5.insert(0,select['Contact No.'])


def Add():
    std_id = e1.get()
    std_name = e2.get()
    contribution = e3.get()
    work_done = e4.get()
    contact_no = e5.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="project_members")
    mycursor=mysqldb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS members (std_ID VARCHAR(11) primary key NOT NULL, std_name VARCHAR(30), contribution INT(10), work_done VARCHAR(30) , contact_no BIGINT )")

    try:
       
       sql = "INSERT INTO  members (std_id,std_name,contribution,work_done,contact_no) VALUES (%s, %s, %s, %s, %s)"
       val = (std_id,std_name,contribution,work_done,contact_no)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Student inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e1.focus_set()
       #show()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()
    show()

def update():
    std_id = e1.get()
    std_name = e2.get()
    contribution = e3.get()
    work_done = e4.get()
    contact_no = e5.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="project_members")
    mycursor=mysqldb.cursor()

    try:
       sql = "Update  members set std_name = %s,contribution = %s,work_done = %s,contact_no = %s where std_id= %s"
       val = (std_name,contribution,work_done,contact_no,std_id)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updateddddd successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e1.focus_set()
       #show()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()
    show()

def delete():
    stdid = e1.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="project_members")
    mycursor=mysqldb.cursor()

    try:
       sql = "delete from members where std_id = %s"
       val = (stdid,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleteeeee successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e1.focus_set()
       #show()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()
    show()
    
def get():
    if(e1.get() == ""):
        messagebox.showinfo("Fetch status","Student ID is compolsary for get the value")
    else:
        stdid=e1.get();
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="project_members")
        mycursor=mysqldb.cursor()
        query=("select * from members where std_id=%s")
        value=(stdid,)
        mycursor.execute(query,value)
        rows=mycursor.fetchall()

        for row in rows:
            e2.insert(0,row[1])
            e3.insert(0,row[2])
            e4.insert(0,row[3])
            e5.insert(0,row[4])
            
        mysqldb.close();


def clear():
    for item in listBox.get_children():
        listBox.delete(item)

def show():
        clear()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="project_members")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT * FROM members")
        records = mycursor.fetchall()
        #print(records)

        for i, (std_id,std_name, contribution, work_done, contact_no) in enumerate(records, start=1):
            listBox.insert("", "end", values=(std_id,std_name, contribution, work_done, contact_no))
            mysqldb.close()

def refresh():
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e1.focus_set()
    

#root = Tk()
root= tb.Window(themename="morph")
root.title("Project Members")
root.geometry("1020x500")
root.resizable(False,False)
global e1
global e2
global e3
global e4
global e5

tk.Label(root, text="Project Members", font=(None, 30)).place(x=500, y=50)

tb.Label(root, text="Student ID",bootstyle="dark").place(x=10, y=10)
tb.Label(root, text="Student Name",bootstyle="dark").place(x=10, y=40)
tb.Label(root, text="Contribution",bootstyle="dark").place(x=10, y=70)
tb.Label(root, text="Work_done",bootstyle="dark").place(x=10, y=100)
tb.Label(root, text="Contact No.",bootstyle="dark").place(x=10, y=130)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

e5 = Entry(root)
e5.place(x=140, y=130)

Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=160)
Button(root, text="update",command = update,height=3, width= 13).place(x=140, y=160)
Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=160)
Button(root, text="Search",command = get,height=3, width= 13).place(x=360, y=160)
Button(root, text="Refresh",command = refresh,height=3, width= 13).place(x=470, y=430)

cols = ('Student ID', 'Student Name', 'Contribution(Rs)','Work_done','Contact No.')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=230)

show()
listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()
