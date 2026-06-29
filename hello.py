import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("電卓")
        self.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        self._build_display()
        self._build_buttons()

    def _build_display(self):
        display = tk.Entry(
            self,
            textvariable=self.display_var,
            font=("Helvetica", 24),
            bd=8,
            relief="ridge",
            justify="right",
            state="readonly",
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew")

    def _build_buttons(self):
        # (ラベル, 行, 列)
        buttons = [
            ("C", 1, 0), ("←", 1, 1), ("/", 1, 2), ("*", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("-", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("+", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("=", 4, 3),
            ("0", 5, 0), (".", 5, 1),
        ]

        for (text, row, col) in buttons:
            colspan = 2 if text == "0" else 1
            btn = tk.Button(
                self,
                text=text,
                font=("Helvetica", 18),
                width=5,
                height=2,
                command=lambda t=text: self._on_click(t),
            )
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew")

    def _on_click(self, key):
        if key == "C":
            self.expression = ""
            self.display_var.set("0")
        elif key == "←":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression or "0")
        elif key == "=":
            self._calculate()
        else:
            self.expression += key
            self.display_var.set(self.expression)

    def _calculate(self):
        try:
            # 四則演算のみ許可
            allowed = set("0123456789+-*/. ")
            if not self.expression or not set(self.expression) <= allowed:
                raise ValueError

            result = eval(self.expression, {"__builtins__": {}}, {})
            self.display_var.set(str(result))
            self.expression = str(result)
        except ZeroDivisionError:
            self.display_var.set("0で除算不可")
            self.expression = ""
        except Exception:
            self.display_var.set("エラー")
            self.expression = ""


if __name__ == "__main__":
    Calculator().mainloop()
