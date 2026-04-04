#1.Create a simple Tkinter window with a title and fixed size.
import tkinter as tk

# Create main window
root = tk.Tk()

# Set window title
root.title("My First Tkinter Window")

# Set fixed window size (width x height)
root.geometry("400x200")

# Disable resizing (fix the size)
root.resizable(False, False)

# Add a label inside window
label = tk.Label(root,text="Welcome to Tkinter GUI",font=("Arial",14))
label.pack(pady=50)

# Run the application
root.mainloop()