import tkinter as tk
from math import *

# Evaluasi Ekspresi
def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Fungsi untuk Menambahkan Input
def press_key(key):
    entry.insert(tk.END, key)

# Fungsi Menghapus Input
def clear():
    entry.delete(0, tk.END)

# Fungsi Menghapus Satu Karakter
def backspace():
    entry.delete(len(entry.get()) - 1, tk.END)

# Membuat Window
app = tk.Tk()
app.title("Scientific Calculator")
app.geometry("375x700")
app.config(bg="#1C1C1C")

# Entry Display
entry = tk.Entry(app, font=("Arial", 30), bd=10, insertwidth=2, width=15, borderwidth=0, bg="#505050", fg="white", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Tombol Kalkulator Scientific 
buttons = [
    ('C', 1, 0, '#A5A5A5'), ('⌫', 1, 1, '#A5A5A5'), ('%', 1, 2, '#A5A5A5'), ('/', 1, 3, '#FF9500'),
    ('7', 2, 0, '#333333'), ('8', 2, 1, '#333333'), ('9', 2, 2, '#333333'), ('*', 2, 3, '#FF9500'),
    ('4', 3, 0, '#333333'), ('5', 3, 1, '#333333'), ('6', 3, 2, '#333333'), ('-', 3, 3, '#FF9500'),
    ('1', 4, 0, '#333333'), ('2', 4, 1, '#333333'), ('3', 4, 2, '#333333'), ('+', 4, 3, '#FF9500'),
    ('0', 5, 0, '#333333'), ('.', 5, 1, '#333333'), ('=', 5, 2, '#FF9500')
]

scientific_buttons = [
    ('sin', 6, 0, '#4A4A4A'), ('cos', 6, 1, '#4A4A4A'), ('tan', 6, 2, '#4A4A4A'), ('log', 6, 3, '#4A4A4A'),
    ('sqrt', 7, 0, '#4A4A4A'), ('exp', 7, 1, '#4A4A4A'), ('pi', 7, 2, '#4A4A4A'), ('e', 7, 3, '#4A4A4A')
]

# style button
def create_rounded_button(text, row, col, color, command):
    btn = tk.Button(app, text=text, padx=20, pady=20, font=("Arial", 20), bg=color, fg="white",
                    command=command, borderwidth=0, relief='flat', highlightbackground=color, highlightthickness=2)
    btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
    btn.config(borderwidth=1, relief="ridge", highlightbackground=color, highlightthickness=2, highlightcolor=color)

# button
for (text, row, col, color) in buttons + scientific_buttons:
    if text == '=':
        create_rounded_button(text, row, col, color, evaluate_expression)
    elif text == 'C':
        create_rounded_button(text, row, col, color, clear)
    elif text == '⌫':
        create_rounded_button(text, row, col, color, backspace)
    else:
        create_rounded_button(text, row, col, color, lambda t=text: press_key(t + '(' if text in ['sin', 'cos', 'tan', 'log', 'sqrt', 'exp'] else t))

# kolom baris
for i in range(8):
    app.grid_rowconfigure(i, weight=1)
for i in range(4):
    app.grid_columnconfigure(i, weight=1)

# run apps
app.mainloop()
