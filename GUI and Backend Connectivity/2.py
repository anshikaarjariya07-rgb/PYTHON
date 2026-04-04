#2.Design a GUI based basic calculator for performing basic arithmetic operations.
import tkinter as tk

#Function for addition
def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text="Result: " + str(num1 + num2))

#Function for subtraction
def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text="Result: " + str(num1 - num2))

#Function for multiplication
def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text="Result: " + str(num1 * num2))

#Function for division
def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if num2 == 0:
        result_label.config(text="Result:Cannot be divided by zero")
    else:
        result_label.config(text="Result: " + str(num1 / num2))

#Create main window
window = tk.Tk()
window.title("Basic Calculator")
window.geometry("350x350")
window.resizable(False,False)

#Label for first number
label1 = tk.Label(window,text="Enter First Number")
label1.pack(pady=5)

#Entry for first number
entry1 = tk.Entry(window)
entry1.pack(pady=5)

#Label for Second number
label2 = tk.Label(window,text="Enter Second Number")
label2.pack(pady=5)

#Entry for second number
entry2 = tk.Entry(window)
entry2.pack(pady=5)

#Buttons for operations
btn_add = tk.Button(window,text="Add",width=10,command=add)
btn_add.pack(pady=5)

btn_subtract = tk.Button(window,text="Subtract",width=10,command=subtract)
btn_subtract.pack(pady=5)

btn_multiply = tk.Button(window,text="Multiply",width=10,command=multiply)
btn_multiply.pack(pady=5)

btn_divide = tk.Button(window,text="Divide",width=10,command=divide)
btn_divide.pack(pady=5)

#Label to display result
result_label=tk.Label(window,text="Result: ",font=("Arial",12))
result_label.pack(pady=10)

#Run the window
window.mainloop()