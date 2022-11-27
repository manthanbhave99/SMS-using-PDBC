def f1():
	entAddRno.focus()
	root.withdraw()
	adst.deiconify()

def f2():
	adst.withdraw()
	root.deiconify()

def f3():
	stdata.delete(1.0, END)
	root.withdraw()
	vist.deiconify()
	con = None
	try:
		con = connect('system/abc123')
		cursor = con.cursor()
		sql = "select * from prostud"
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = ""
		for d in data:
			msg = msg + " RNO. " + str(d[0]) + " NAME " + str(d[1]) + " MARKS " + str(d[2]) + '\n'
		stdata.insert(INSERT, msg)
	except DatabaseError as e:
		con.rollback()
		print("issue  ", e)
	finally:
		if con is not None:
			con.close()

def f4():
	vist.withdraw()
	root.deiconify()

def f5():
	con = None
	try:
		
			con = connect('system/abc123')
			rn = int(entAddRno.get())
			name = entAddName.get()
			m = int(entAddMarks.get())
			if name.isalpha():
				if (m <=100):
					cursor = con.cursor()
					sql = "insert into prostud values('%d', '%s', '%d')"
					args = (rn, name, m)
					cursor.execute(sql % args)
					con.commit()
					messagebox.showinfo("SUCCESS ", " RECORD INSERTED")
					entAddRno.delete(0, END)
					entAddName.delete(0, END)
					entAddMarks.delete(0, END)
					entAddRno.focus()
				else:
					messagebox.showerror("FAILED", "ENTER MARKS BETWEEN 0 - 100")
					entAddMarks.delete(0, END)
					entAddMarks.focus()
			else:
				messagebox.showerror("FAILED", "NAME MUST HAVE STRING")
				entAddName.delete(0, END)
				entAddName.focus()			
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("FAILED ", " DUPLICATE KEY")
		entAddRno.delete(0, END)
		entAddRno.focus()
	except ValueError:
		messagebox.showerror("FAILED", "ENTER INTEGERS ONLY")
		entAddRno.delete(0, END)
		entAddRno.focus()
	finally:
		if con is not None:
			con.close()


def f6():
	entUpRno.focus()
	root.withdraw()
	upst.deiconify()

def f7():
	con = None
	try:
		con = connect('system/abc123')
		rn = int(entUpRno.get())
		name = entUpName.get()
		m= int(entUpMarks.get())
		if name.isalpha():
			if (m <=100):
				cursor = con.cursor()
				sql = "update prostud set name = '%s', marks = '%d' where rn = '%d'"
				args = (name, m, rn)
				cursor.execute(sql % args)
				con.commit()
				messagebox.showinfo("SUCCESS ", " RECORD UPDATED")
				entUpRno.delete(0, END)
				entUpName.delete(0, END)
				entUpMarks.delete(0, END)
				entUpRno.focus()
			else:
				messagebox.showerror("FAILED", "ENTER MARKS BETWEEN 0 - 100")
				entUpMarks.delete(0, END)
				entUpMarks.focus()
		else:
			messagebox.showerror("FAILED", "NAME MUST HAVE STRING")
			entUpName.delete(0, END)
			entUpName.focus()	
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("FAILED ", " ROLL NO. NOT FOUND")
		entUpRno.delete(0, END)
		entUpRno.focus()
	except ValueError:
		messagebox.showerror("FAILED", "ENTER INTEGERS ONLY")
		entUpRno.delete(0, END)
		entUpRno.focus()
	finally:
		if con is not None:
			con.close()

def f8():
	upst.withdraw()
	root.deiconify()

def f9():
	entDelRno.focus()
	root.withdraw()
	delst.deiconify()

def f10():
  con = None
	try:
		con = connect('system/abc123')
		cursor = con.cursor()
		rn = int(entDelRno.get())
		sql = "delete from prostud where rn = '%d'"
		args = (rn)
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("SUCCESS ", " RECORD DELETED")
		entDelRno.delete(0, END)
		entDelRno.focus()
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("FAILED ", " ROLL NO. NOT FOUND")
		entDelRno.delete(0, END)
		entDelRno.focus()
	except ValueError:
		messagebox.showerror("FAILED", "ENTER INTEGERS ONLY")
		entDelRno.delete(0, END)
		entDelRno.focus()

	finally:
		if con is not None:
			con.close()

def f11():
  delst.withdraw()
	root.deiconify()

def f12():
	import cx_Oracle
	import pandas as pd
	import matplotlib.pyplot as plt
	import numpy as np
  
  con = None
	try:
		con = cx_Oracle.connect('system/abc123')
		cursor = con.cursor()
		sql= "select * from prostud"
		result = cursor.execute(sql)
		row=cursor.fetchall()
		nlist = []
		mlist = []
		for i in row:
		#	print(i[1],i[2])
			nlist.append(i[1])
			mlist.append(i[2])
		#	print(nlist, mlist)
		
		x = np.arange(len(nlist))
		plt.bar(x, mlist, label='MATHS', color = 'yellow', edgecolor = 'red', linewidth = 2,  hatch= '\\')
		plt.xticks(x, nlist)
		plt.xlabel("NAMES")
		plt.ylabel("MARKS")
		plt.title("STUDENT'S BAR GRAPH")
		plt.grid()
		plt.show()
			
	except DatabaseError as e:
		con.rollback()
		print("issue  ", e)
	finally:
		if con is not None:
			con.close()


  
  
  
