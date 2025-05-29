import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Calculator")
        self.root.geometry("320x440")
        self.root.resizable(False, False)

        self.expression = ""

        self.create_display()
        self.create_buttons()
        self.bind_keys()

    def create_display(self):
        self.input_text = tk.StringVar()
        self.input_field = tk.Entry(self.root, textvariable=self.input_text,
                                    font=('Arial', 24), bd=10, insertwidth=2,
                                    width=14, borderwidth=4, relief='ridge',
                                    justify='right')
        self.input_field.pack(pady=20, padx=10, fill='x')

    def create_buttons(self):
        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        buttons = [
            ["C", "←", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["00", "0", ".", "="]
        ]

        for row in buttons:
            row_frame = tk.Frame(btns_frame)
            row_frame.pack(expand=True, fill='both')
            for btn_text in row:
                btn = tk.Button(row_frame, text=btn_text, font=('Arial', 18),
                                bd=2, relief='groove', command=lambda x=btn_text: self.click(x))
                btn.pack(side='left', expand=True, fill='both', padx=2, pady=2)

    def bind_keys(self):
        self.root.bind("<Return>", lambda e: self.click("="))
        self.root.bind("<BackSpace>", lambda e: self.click("←"))
        for key in "0123456789+-*/.=C":
            self.root.bind(key, self.keypress)

    def keypress(self, event):
        self.click(event.char)

    def click(self, key):
        if key == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        elif key == "C":
            self.expression = ""
            self.input_text.set("")
        elif key == "←":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        else:
            self.expression += key
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
