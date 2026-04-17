#3.Design a GUI for student registration for a course and store these details in a database. 
# Use Tkinter for UI, SQLite/MySQL for database storage.
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database Setup
def init_db():
    conn = sqlite3.connect("university.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, roll TEXT, course TEXT)''')
    conn.commit()
    conn.close()

def register_student():
    name = entry_name.get()
    roll = entry_roll.get()
    course = entry_course.get()

    if name == "" or roll == "" or course == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    conn = sqlite3.connect("university.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, roll, course) VALUES (?, ?, ?)", (name, roll, course))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Student Registered Successfully!")
    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    entry_course.delete(0, tk.END)

# UI Setup
root = tk.Tk()
root.title("Student Registration")
root.geometry("300x250")

tk.Label(root, text="Student Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Roll Number:").pack(pady=5)
entry_roll = tk.Entry(root)
entry_roll.pack()

tk.Label(root, text="Course:").pack(pady=5)
entry_course = tk.Entry(root)
entry_course.pack()

tk.Button(root, text="Register", command=register_student, bg="green", fg="white").pack(pady=20)

init_db()
root.mainloop()
