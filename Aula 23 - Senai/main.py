import tkinter as tk

def somar():
    n1 = entry_n get()
    n2 = entry_n2.get()
    result = n1 + n2


root = tk.Tk()
root.title('Soma')

label_n1 = tk.Label()

import tkinter as tk

def press_key(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(key))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro")

root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "C":
        tk.Button(root, text=button, width=5, height=2, command=clear).grid(row=row_val, column=col_val)
    elif button == "=":
        tk.Button(root, text=button, width=5, height=2, command=calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, width=5, height=2, command=lambda key=button: press_key(key)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()


import tkinter as tk

def soma():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Digite números válidos")

root = tk.Tk()

root.title("Calculadora de Soma")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_num1 = tk.Label(frame, text="Número 1:")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(frame)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(frame, text="Número 2:")
label_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(frame)
entry_num2.grid(row=1, column=1)

button_calcular = tk.Button(frame, text="Calcular Soma", command=soma,)
button_calcular.grid(row=2, columnspan=2)

label_resultado = tk.Label(frame, text="")
label_resultado.grid(row=3, columnspan=2)

root.mainloop()
