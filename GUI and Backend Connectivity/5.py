#5.Design a login and signup authentication system.
import tkinter as tk
from tkinter import messagebox
import sqlite3

def init_db():
    conn = sqlite3.connect("auth.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
    conn.commit()
    conn.close()

def signup():
    user = entry_user.get()
    pw = entry_pw.get()
    if user and pw:
        try:
            conn = sqlite3.connect("auth.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users VALUES (?, ?)", (user, pw))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Account Created!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "User already exists!")
    else:
        messagebox.showwarning("Error", "Fill all fields")

def login():
    user = entry_user.get()
    pw = entry_pw.get()
    conn = sqlite3.connect("auth.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pw))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        messagebox.showinfo("Login Success", f"Welcome {user}!")
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")

# UI
root = tk.Tk()
root.title("Auth System")
root.geometry("250x200")

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pw = tk.Entry(root, show="*")
entry_pw.pack()

tk.Button(root, text="Login", command=login, width=10).pack(pady=5)
tk.Button(root, text="Sign Up", command=signup, width=10).pack()

init_db()
root.mainloop()
