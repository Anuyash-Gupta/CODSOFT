import tkinter as tk
from tkinter import messagebox

def perform_addition():
    try:
        anuyash1 = float(entry_anuyash1.get())
        anuyash2 = float(entry_anuyash2.get())
        result_box.delete(0, tk.END)
        result_box.insert(0, str(anuyash1 + anuyash2))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

def perform_subtraction():
    try:
        anuyash1 = float(entry_anuyash1.get())
        anuyash2 = float(entry_anuyash2.get())
        result_box.delete(0, tk.END)
        result_box.insert(0, str(anuyash1 - anuyash2))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

def perform_multiplication():
    try:
        anuyash1 = float(entry_anuyash1.get())
        anuyash2 = float(entry_anuyash2.get())
        result_box.delete(0, tk.END)
        result_box.insert(0, str(anuyash1 * anuyash2))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

def perform_division():
    try:
        anuyash1 = float(entry_anuyash1.get())
        anuyash2 = float(entry_anuyash2.get())
        if anuyash2 == 0:
            messagebox.showerror("Division Error", "Division by zero is not allowed.")
            return
        result_box.delete(0, tk.END)
        result_box.insert(0, str(anuyash1 / anuyash2))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")


harsh = tk.Tk()
harsh.title("Anuyash Calculator")


tk.Label(harsh, text="Enter First Number:").grid(row=0, column=0, padx=6, pady=6)
entry_anuyash1 = tk.Entry(harsh)
entry_anuyash1.grid(row=0, column=1, padx=6, pady=6)

tk.Label(harsh, text="Enter Second Number:").grid(row=1, column=0, padx=6, pady=6)
entry_anuyash2 = tk.Entry(harsh)
entry_anuyash2.grid(row=1, column=1, padx=6, pady=6)

tk.Label(harsh, text="Result:").grid(row=2, column=0, padx=6, pady=6)
result_box = tk.Entry(harsh)
result_box.grid(row=2, column=1, padx=6, pady=6)


tk.Button(harsh, text="+", width=6, command=perform_addition).grid(row=3, column=0, padx=5, pady=5)
tk.Button(harsh, text="-", width=6, command=perform_subtraction).grid(row=3, column=1, padx=5, pady=5)
tk.Button(harsh, text="×", width=6, command=perform_multiplication).grid(row=4, column=0, padx=5, pady=5)
tk.Button(harsh, text="÷", width=6, command=perform_division).grid(row=4, column=1, padx=5, pady=5)

harsh.mainloop()
