import tkinter as tk
from tkinter import messagebox
import math
import random

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Scientific Calculator")
        self.root.geometry("800x700")  # Adjust the window size to make it compact
        self.root.config(bg="#2c3e50")
        self.root.resizable(True, True)  # Allow window resizing

        self.is_degrees = True  # To track if the calculator is in degrees mode

        # Create the display
        self.display_input = tk.Entry(self.root, font=("Helvetica", 18), borderwidth=0, relief="solid", justify="right", bg="#1c1c1c", fg="#ecf0f1")
        self.display_output = tk.Entry(self.root, font=("Helvetica", 32), borderwidth=0, relief="solid", justify="right", bg="#1c1c1c", fg="#ecf0f1")

        self.display_input.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)
        self.display_output.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

        # Configure the rows and columns to expand dynamically
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)

        # Create the button layout
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3), ('sqrt', 2, 4),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), ('^', 3, 4),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), ('log', 4, 4),
            ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3), ('ln', 5, 4),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('asin', 6, 3), ('acos', 6, 4),
            ('sinh', 7, 0), ('cosh', 7, 1), ('tanh', 7, 2), ('atan', 7, 3), ('atanh', 7, 4),
            ('(', 8, 0), (')', 8, 1), ('C', 8, 2), ('DEL', 8, 3), ('rand', 8, 4),
            ('PI', 9, 0), ('e', 9, 1), ('deg/rad', 9, 2), ('!', 9, 3), ('x!', 9, 4),
            ('C2', 10, 0), ('C3', 10, 1), ('2^', 10, 2), ('log2', 10, 3), ('exp', 10, 4)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Helvetica", 14), fg="#ffffff", relief="flat", 
                               bg="#3498db", activebackground="#2980b9", width=4, height=2,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        for i in range(11):
            self.root.grid_rowconfigure(i + 2, weight=1)
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        current_input = self.display_input.get()

        if char == 'C':
            self.display_input.delete(0, tk.END)
            self.display_output.delete(0, tk.END)
        elif char == 'DEL':
            self.display_input.delete(len(current_input) - 1, tk.END)
        elif char == '=':
            try:
                expression = current_input.replace('^', '**').replace('PI', str(math.pi)).replace('e', str(math.e))
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
                self.display_input.delete(0, tk.END)
                self.display_output.delete(0, tk.END)
                self.display_input.insert(tk.END, current_input)
                self.display_output.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Expression: {str(e)}")
                self.display_input.delete(0, tk.END)
                self.display_output.delete(0, tk.END)
        else:
            self.display_input.insert(tk.END, char)

    def toggle_mode(self):
        self.is_degrees = not self.is_degrees
        if self.is_degrees:
            self.display_input.delete(0, tk.END)
            self.display_input.insert(tk.END, "Degrees Mode")
        else:
            self.display_input.delete(0, tk.END)
            self.display_input.insert(tk.END, "Radians Mode")

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
