from tkinter import*
from tkinter import messagebox
import sqlite3

#definition for the functions
#to add and clear the database
#creater :stiveckamash@gmail.com
#0705698768    0798355947
#A simple student database system that takes their name and the scores via a GUI application

db=sqlite3.connect("student.db")
cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS student_scores(id integer primary key,name text not null,scores integer not null)""")

def add_details():
	newname=sname.get()
	newgrade=sgrade.get()
	try:
		newgrade=int(newgrade)
		cursor.execute("""INSERT INTO student_scores (name,scores) VALUES(?,?)""",(newname,newgrade))
		db.commit()
		error=Label(text="Data addded Successfully!",bg='red',fg='yellow')
		error.place(x=30,y=150,width=250,height=25)

	except Exception as e:
		messagebox.showinfo('error','a digit is needed')
		error=Label(text="Please enter an int datatype in the score field",bg='red',fg='yellow')
		error.place(x=30,y=150,width=250,height=25)

		

	sname.delete(0,END)
	sgrade.delete(0,END)
	sname.focus()

def clear_details():
	sname.delete(0,END)
	sgrade.delete(0,END)
	sname.focus()


#gui definition
win=Tk()
win.title("Students Database System:")
win.geometry("350x400")
win.resizable(0,0)

#labels definition
label_1=Label(text='Enter the Student\'s name: ')
label_1.place(x=30,y=35)
sname=Entry(text="")
sname.place(x=150,y=35,width=200,height=25)
sname.focus()


label_2=Label(text='Enter the Student\'s scores: ')
label_2.place(x=30,y=80)
sgrade=Entry(text="")
sgrade.place(x=150,y=80,width=200,height=25)
sgrade.focus()

add_btn=Button(text='Add',command=add_details,bg='blue')
add_btn.place(x=150,y=120,width=75,height=25)


clear_btn=Button(text='Clear',command=clear_details,bg='red')
clear_btn.place(x=250,y=120,width=75,height=25)


db=sqlite3.connect("student.db")
cursor=db.cursor()

win.mainloop()
db.close()