from tkinter import *
import tkinter
from turtle import down, title
from PIL import ImageTk, Image
import psycopg2

def display(cur):
    table_name=input("Enter table name: ")
    cur.execute("select * from %s",table_name)
    table_window=Tk()
    table_window.title=table_name
    tabel_label=Label(table_window,text=cur.fetchall()).pack()
    table_window.mainloop()


conn=None
cur=None
try:
    conn=psycopg2.connect(host="localhost",database="project",user="postgres",password="test123")
    cur=conn.cursor()

    root=Tk()
    root.title("Namma Metro")
    image_0=Image.open("D:\\dbms_project\\1a5e62cd13279eb4c49e722117250152.jpg")
    backgroud=ImageTk.PhotoImage(image_0)
    root.geometry("900x680")
    lbl=Label(root,image=backgroud)
    lbl.place(x=0,y=0)
    #********************************not change anything above here*************************************************

    label=Label(root,text="Namma Metro",font="arial 40 bold",bg='light blue')
    label.pack()
    def retrieve_input():
        inputValue=textBox.get("1.0","end-1c")
        print(inputValue)

    textBox=Text(root, height=10, width=50)
    textBox.place(x=480,y=200)
    buttonCommit=Button(root, height=1, width=10,font="arial 20 bold",bg='blue',text="execute",
                        command=lambda: retrieve_input())#in command write the function name and define the function every button add command =function_name(parameter required)
    #command=lambda: retrieve_input() >>> just means do this when i press the button
    buttonCommit.place(x=480,y=400)
    b1=Button(text="Update",font="arial 20 bold",bg='blue')#cammand="function_name no need cotes"#
    b2=Button(text="Insert",font="arial 20 bold",bg='blue')#command="function_name")
    b3=Button(text="Delete",font="arial 20 bold",bg='blue')#command="function_name")
    b4=Button(text="Display",font="arial 20 bold",bg='blue',command=lambda:display(cur))
    b6=Button(text="Exit",font='arial 20 bold',command=root.destroy,bg='blue')

    b1.place(x=80,y=600)
    b2.place(x=240,y=600)
    b3.place(x=380,y=600)
    b4.place(x=520,y=600)
    b6.place(x=800,y=600)
    root.resizable(False,False)
    conn.commit()
    #write any anythink above these ******************************************************
    root.mainloop()
except (Exception,psycopg2.DatabaseError) as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    