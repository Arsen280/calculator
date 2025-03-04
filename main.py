import tkinter as tk
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Kalkulačka')
        self.window.geometry('300x500')
        self.window.configure(bg='#f0f0f0')
        self.window.resizable(0, 0)

        self.digit_style = {'bg': '#ffffff', 'fg': '#000000', 'font': ('Arial', 12, 'bold')}
        self.op_style = {'bg': '#e8e8e8', 'fg': '#000000', 'font': ('Arial', 12, 'bold')}
        self.special_style = {'bg': '#ff9500', 'fg': '#ffffff', 'font': ('Arial', 12, 'bold')}

        self.display = tk.Entry(self.window, width=20, justify='right',
                              font=('Arial', 24), bd=10, bg='#ffffff')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        self.create_buttons()

    def create_buttons(self):
        button_list = [
            ('7', self.digit_style), ('8', self.digit_style), ('9', self.digit_style), ('/', self.op_style),
            ('4', self.digit_style), ('5', self.digit_style), ('6', self.digit_style), ('*', self.op_style),
            ('1', self.digit_style), ('2', self.digit_style), ('3', self.digit_style), ('-', self.op_style),
            ('0', self.digit_style), ('.', self.digit_style), ('+/-', self.op_style), ('+', self.op_style),
        ]

        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)
            self.window.grid_rowconfigure(i+1, weight=1)

        row = 1
        col = 0
        for (button_text, style) in button_list:
            button = tk.Button(self.window, text=button_text, width=5, height=2,
                             command=lambda x=button_text: self.click_button(x),
                             **style)
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
            col += 1
            if col > 3:
                col = 0
                row += 1

        equals_button = tk.Button(self.window, text='=', width=5, height=2,
                                command=lambda: self.click_button('='),
                                **self.special_style)
        equals_button.grid(row=row, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

        clear_button = tk.Button(self.window, text='C', width=5, height=2,
                               command=self.clear_display,
                               **self.special_style)
        clear_button.grid(row=row, column=2, columnspan=2, padx=5, pady=5, sticky='nsew')

        row += 1
        functions = [('sin', self.calculate_sin), ('cos', self.calculate_cos), ('tan', self.calculate_tan), ('D', self.calculate_discriminant)]
        col = 0
        for text, func in functions:
            button = tk.Button(self.window, text=text, width=5, height=2,
                               command=lambda f=func, t=text: self.apply_function(f, t),
                               **self.special_style)
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
            col += 1

    def click_button(self, value):
        if value == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "mame error")
        elif value == '+/-':
            try:
                current = self.display.get()
                if current:
                    if current[0] != '-':
                        self.display.insert(0, '-')
                    else:
                        self.display.delete(0, 1)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "mame error")
        else:
            self.display.insert(tk.END, value)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def apply_function(self, func, name):
        try:
            if name == 'D':
                values = self.display.get().split()
                if len(values) != 3:
                    raise ValueError
                a, b, c = map(float, values)
                result = func(a, b, c)
            else:
                value = float(self.display.get())
                result = func(value)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "error")

    def calculate_sin(self, value):
        return round(math.sin(math.radians(value)), 6)

    def calculate_cos(self, value):
        return round(math.cos(math.radians(value)), 6)

    def calculate_tan(self, value):
        return "undefined" if math.cos(math.radians(value)) == 0 else round(math.tan(math.radians(value)), 6)

    def calculate_discriminant(self, a, b, c):
        return (b ** 2) - (4 * a * c)

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    calc = Calculator()
    calc.run()
