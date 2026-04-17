#4.Create a GUI based task manager where users can add, edit and remove tasks. 
# Use Tkinter (buttons, listbox), SQLite/MySQL (task storage).
import tkinter as tk
from tkinter import messagebox
import sqlite3

def init_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)")
    conn.commit()
    conn.close()

def add_task():
    task = entry_task.get()
    if task:
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        conn.close()
        entry_task.delete(0, tk.END)
        load_tasks()
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def load_tasks():
    listbox_tasks.delete(0, tk.END)
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    for row in cursor.fetchall():
        listbox_tasks.insert(tk.END, f"{row[0]}. {row[1]}")
    conn.close()

def delete_task():
    try:
        selected = listbox_tasks.get(listbox_tasks.curselection())
        task_id = selected.split(".")[0]
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        conn.close()
        load_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

root = tk.Tk()
root.title("B.Tech Task Manager")

entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Delete Selected", command=delete_task).pack()

listbox_tasks = tk.Listbox(root, width=50)
listbox_tasks.pack(pady=10)

init_db()
load_tasks()
root.mainloop()
