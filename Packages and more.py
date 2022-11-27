from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import *

# root frontend creation
root = Tk()
root.title("STUDENT MANAGEMENT SYSTEM")
root.geometry("1200x600+50+10")
root.resizable(False, False)
root.configure(background="orange")

#  Functions are defined
# def f1() ---> def f12()

import socket
import requests

# Connection established...
try:
	socket.create_connection(("www.google.com", 80))
	print("INTERNET is ON")
	res = requests.get("https://ipinfo.io")
	data = res.json()
  
 if socket.create_connection(("www.google.com", 80)) :

	btnAdd = Button(root, text = "ADD", font=('comic sans ms', 18, 'bold italic'), width=10, command=f1)
	btnView = Button(root, text = "VIEW", font=('comic sans ms', 18, 'bold italic'), width=10,command=f3)
	btnUp = Button(root, text = "UPDATE", font=('comic sans ms', 18, 'bold italic'), width=10, command=f6)
	btnDel = Button(root, text = "DELETE", font=('comic sans ms', 18, 'bold italic'), width=10, command=f9)
	btnGph = Button(root, text = "GRAPH", font=('comic sans ms', 18, 'bold italic'), width=10, command=f12)

	lbCity = Label(root, text = "CITY ", font=('comic sans ms', 18, 'bold'))
	lblCity = Label(root, text = city, font=('arial', 18, 'bold') )
	lbTemp = Label(root, text = "TEMP ", font=('comic sans ms', 18, 'bold'))
	lblTmp = Label(root, text = temp, font=('arial', 18, 'bold'))
	
	lbQte = Label(root, text = "QUOTE of The DAY ", font=('comic sans ms', 18, 'bold'))
	lblQte = Label(root, text = msg, font=('arial', 10, 'bold'), width = 500 )
	

	btnAdd.pack(pady=10)
	btnView.pack(pady=10)
	btnUp.pack(pady=10)
	btnDel.pack(pady=10)
	btnGph.pack()
	lbCity.pack(side = LEFT )
	lblCity.pack(side=LEFT, padx=10)
	lblTmp.pack(side=RIGHT, padx=10)
	lbTemp.pack(side = RIGHT)
	lbQte.pack(pady=10)
	lblQte.pack(pady= 10)


adst = Toplevel(root)
adst.title("ADD STUDENT")
adst.geometry("500x500+500+100")
adst.resizable(False, False)
adst.configure(background="yellow")

lbAddRno = Label(adst, text = "ENTER ROLL NUMBER", font=('comic sans ms', 18, 'bold'))
entAddRno = Entry(adst, bd=2, font=('arial', 18, 'bold'))
lbAddName = Label(adst, text = "ENTER NAME", font=('comic sans ms', 18, 'bold'))
entAddName = Entry(adst, bd=5, font=('arial', 18, 'bold'))
lbAddMarks = Label(adst, text = "ENTER MARKS", font=('comic sans ms', 18, 'bold'))
entAddMarks = Entry(adst, bd=5, font=('arial', 18, 'bold'))
btnAddSave = Button(adst, text="SAVE",font=('arial', 18, 'bold'), command=f5)
btnAddBack = Button(adst, text= "BACK", font=('arial', 18, 'bold'), command=f2)

lbAddRno.pack(pady=10)
entAddRno.pack(pady=10)
lbAddName.pack(pady=10)
entAddName.pack(pady=10)
lbAddMarks.pack(pady=10)
entAddMarks.pack(pady=10)
btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)

adst.withdraw()


vist = Toplevel(root)
vist.title("VIEW STUDENT")
vist.geometry("450x400+500+200")
vist.resizable(False, False)
vist.configure(background="red")

stdata = scrolledtext.ScrolledText(vist,width=35, height=20)
btnViewBack = Button(vist, text= "BACK", font=('arial', 18, 'bold'), command=f4)

stdata.pack(pady=10)
btnViewBack.pack(pady=10)
vist.withdraw()

upst = Toplevel(root)
upst.title("UPDATE STUDENT")
upst.geometry("500x500+500+100")
upst.resizable(False, False)
upst.configure(background="sky blue")

lbUpRno = Label(upst, text = "ENTER ROLL NUMBER", font=('comic sans ms', 18, 'bold'))
entUpRno = Entry(upst, bd=2, font=('arial', 18, 'bold'))
lbUpName = Label(upst, text = "ENTER NAME", font=('comic sans ms', 18, 'bold'))
entUpName = Entry(upst, bd=5, font=('arial', 18, 'bold'))
lbUpMarks = Label(upst, text = "ENTER MARKS", font=('comic sans ms', 18, 'bold'))
entUpMarks = Entry(upst, bd=5, font=('arial', 18, 'bold'))
btnUpSave = Button(upst, text="SAVE",font=('arial', 18, 'bold'), command=f7)
btnUpBack = Button(upst, text= "BACK", font=('arial', 18, 'bold'), command=f8)

lbUpRno.pack(pady=10)
entUpRno.pack(pady=10)
lbUpName.pack(pady=10)
entUpName.pack(pady=10)
lbUpMarks.pack(pady=10)
entUpMarks.pack(pady=10)
btnUpSave.pack(pady=10)
btnUpBack.pack(pady=10)
upst.withdraw()


delst = Toplevel(root)
delst.title("DELETE STUDENT")
delst.geometry("400x400+500+200")
delst.resizable(False, False)
delst.configure(background="sky blue")

lbDelRno = Label(delst, text = "ENTER ROLL NUMBER", font=('comic sans ms', 18, 'bold'))
entDelRno = Entry(delst, bd=2, font=('arial', 18, 'bold'))

btnDel = Button(delst, text="DELETE",font=('arial', 18, 'bold'), command=f10)
btnDelBack = Button(delst, text= "BACK", font=('arial', 18, 'bold'), command=f11)

lbDelRno.pack(pady=10)
entDelRno.pack(pady=10)
btnDel.pack(pady=10)
btnDelBack.pack(pady=10)
delst.withdraw()



root.mainloop()
