import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.create_ui()

    def create_ui(self):
        result_entry = tk.Entry(self.root, textvariable=self.result_var, font=("Helvetica", 16), bd=10, insertwidth=4, width=14, justify='right')
        result_entry.grid(row=0, column=0, columnspan=4)

        button_texts = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for (text, row, col) in button_texts:
            button = tk.Button(self.root, text=text, padx=20, pady=20, font=("Helvetica", 16), command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, sticky='nsew')

        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_columnconfigure(4, weight=1)

    def button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            new_text = current_text + char
            self.result_var.set(new_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
