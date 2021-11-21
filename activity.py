import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry('500x500')

todoListLabel = Label(window,text="Todo List")

databaseObject = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="db_todolist"
)

cursor = databaseObject.cursor()

# GROUP: Fetch tasks from table in database
sqlStatement = "SELECT fld_task FROM tbl_tasks"
cursor.execute(sqlStatement)
myResult = cursor.fetchall()

# GROUP: Map task (tuple from the array) to `tasks` list to set up in list box
tasks = []
for task in myResult:
	tasks.append(task[0])

# GROUP: Set up tasks to list box
tasksList = tuple(tasks)
listOfTasks = tk.StringVar(value=tasksList)
listbox = Listbox(window,listvariable=listOfTasks)

# GROUP: Create label and entry for the task
taskLabel = tk.Label(text = "Task:")
taskEntry = tk.Entry()


def addTask():
	# GROUP: If task entered from the entry is not blank, insert to table.
	task = taskEntry.get()
	if (task.strip() != ""):
		sqlStatement = "INSERT INTO tbl_tasks(fld_task) VALUES(%s)"
		data = (task.strip(),)
		cursor.execute(sqlStatement, data)
		databaseObject.commit()
		listbox.insert(END,task.strip())
		taskEntry.delete(0,END)
	else:
		messagebox.showerror(title="Invalid Task",message="Please enter a valid task. Thank you.")

def deleteSelectedTask():
	# GROUP: Delete task when available in list.
	try:
		index = listbox.curselection()
		if (not index is None):
			sqlStatement = "DELETE FROM tbl_tasks WHERE fld_task = %s"
			data = (listbox.get(index),)
			cursor.execute(sqlStatement, data)
			databaseObject.commit()
			listbox.delete(index)
		else:
			messagebox.showerror(title="Invalid Delete",message="Please select a valid task to delete. Thank you.")
	except:
		messagebox.showerror(title="Invalid Delete",message="Please select a valid task to delete. Thank you.")

addTaskButton = tk.Button(master=window,text="Add Task",command=addTask)
deleteTaskButton = tk.Button(master=window,text="Delete Task",command=deleteSelectedTask)

# GROUP: Pack all widgets needed.
todoListLabel.pack()
listbox.pack()
taskLabel.pack()
taskEntry.pack()
addTaskButton.pack()
deleteTaskButton.pack()


window.mainloop()