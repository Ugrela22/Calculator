import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.expression = ""

        self.input_text = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Input field
        input_field = tk.Entry(self.root, textvariable=self.input_text, font=('Arial', 18), bd=10,
                               insertwidth=2, width=14, borderwidth=4, justify='right')
        input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, sticky="nsew")

        # Button layout
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '^', '+'),
            ('(', ')', '√', '='),
            ('C',)
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                btn = tk.Button(self.root, text=char, padx=20, pady=20, font=('Arial', 14),
                                command=lambda ch=char: self.on_click(ch))
                btn.grid(row=r+1, column=c, sticky="nsew")

        # Make the grid responsive
        for i in range(len(buttons) + 1):  # rows
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):  # columns
            self.root.grid_columnconfigure(j, weight=1)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '=':
            try:
                expr = self.expression.replace('^', '**')
                if '√' in expr:
                    expr = expr.replace('√', 'math.sqrt')
                result = eval(expr, {"math": math})
                self.input_text.set(str(result))
                self.expression = str(result)
            except Exception:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()