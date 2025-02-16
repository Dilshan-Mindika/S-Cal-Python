import tkinter as tk
from tkinter import messagebox
import math
import random

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Scientific Calculator")
        self.root.geometry("600x800")
        self.root.config(bg="#2c3e50")
        self.root.resizable(False, False)

        self.is_degrees = True  # To track if the calculator is in degrees mode

        # Create the display
        self.display = tk.Entry(self.root, font=("Helvetica", 32), borderwidth=0, relief="solid", justify="right", bg="#1c1c1c", fg="#ecf0f1")
        self.display.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=20)

        # Add some padding and shadow effect
        self.display.config(bd=0, relief="flat")

        # Create the button layout
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('log', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('ln', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('asin', 5, 3), ('acos', 5, 4),
            ('sinh', 6, 0), ('cosh', 6, 1), ('tanh', 6, 2), ('atan', 6, 3), ('atanh', 6, 4),
            ('(', 7, 0), (')', 7, 1), ('C', 7, 2), ('DEL', 7, 3), ('rand', 7, 4),
            ('PI', 8, 0), ('e', 8, 1), ('deg/rad', 8, 2), ('!', 8, 3), ('x!', 8, 4),
            ('C2', 9, 0), ('C3', 9, 1), ('2^', 9, 2), ('log2', 9, 3), ('exp', 9, 4)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Helvetica", 18), fg="#ffffff", relief="flat", 
                               bg="#3498db", activebackground="#2980b9", width=5, height=2,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)

        for i in range(10):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

        # Adjust button size and borders for more spacing
        self.root.grid_rowconfigure(0, weight=1)

    def on_button_click(self, char):
        current = self.display.get()

        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == 'DEL':
            self.display.delete(len(current) - 1, tk.END)
        elif char == '=':
            try:
                expression = current.replace('^', '**').replace('PI', str(math.pi)).replace('e', str(math.e))
                expression = expression.replace('log', 'math.log10').replace('ln', 'math.log')
                expression = expression.replace('sin', 'math.sin').replace('cos', 'math.cos')
                expression = expression.replace('tan', 'math.tan').replace('sqrt', 'math.sqrt')
                expression = expression.replace('asin', 'math.asin').replace('acos', 'math.acos')
                expression = expression.replace('atan', 'math.atan').replace('sinh', 'math.sinh')
                expression = expression.replace('cosh', 'math.cosh').replace('tanh', 'math.tanh')
                expression = expression.replace('atanh', 'math.atanh').replace('rand', 'random.random')
                expression = expression.replace('deg/rad', 'self.toggle_mode()')  # Toggle degree/radian

                # Special handling for factorial
                if '!' in expression:
                    expression = expression.replace('!', '')
                    expression = f'math.factorial({expression})'

                result = str(eval(expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Expression: {str(e)}")
                self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, char)

    def toggle_mode(self):
        self.is_degrees = not self.is_degrees
        if self.is_degrees:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Degrees Mode")
        else:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Radians Mode")

    # Custom factorial function
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
