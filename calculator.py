# GUI Calculator using Tkinter

import tkinter as tk

# Function to handle button click
def click(event):
    global expression
    expression = expression + str(event.widget.cget("text"))
    input_text.set(expression)

# Function to evaluate the expression
def evaluate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result  # allow further calculations
    except ZeroDivisionError:
        input_text.set("Error: Division by zero")
        expression = ""
    except Exception:
        input_text.set("Error")
        expression = ""

# Function to clear input
def clear():
    global expression
    expression = ""
    input_text.set("")

# Main window
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("400x500")

expression = ""
input_text = tk.StringVar()

# Input field
input_frame = tk.Frame(root, width=400, height=50, bd=5, relief=tk.RIDGE)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('Arial', 20), textvariable=input_text, bd=5, relief=tk.RIDGE, justify='right')
input_field.pack(fill=tk.BOTH, expand=True)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text == '=':
            btn = tk.Button(button_frame, text=btn_text, width=10, height=3, bd=2, font=('Arial', 15), fg='white', bg='green')
            btn.grid(row=i, column=j, padx=3, pady=3)
            btn.bind('<Button-1>', lambda event: evaluate())
        elif btn_text == 'C':
            btn = tk.Button(button_frame, text=btn_text, width=44, height=3, bd=2, font=('Arial', 15), fg='white', bg='blue', command=clear)
            btn.grid(row=i, column=0, columnspan=4, padx=3, pady=3)
        else:
            btn = tk.Button(button_frame, text=btn_text, width=10, height=3, bd=2, font=('Arial', 15))
            btn.grid(row=i, column=j, padx=3, pady=3)
            btn.bind('<Button-1>', click)

# Run the GUI loop
root.mainloop()
