import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.shift_mode = False
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, width=30, borderwidth=5, font=("Arial", 14))
        self.entry.grid(row=0, column=0, columnspan=6)

        buttons = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
            ('sin',1,4), ('cos',2,4), ('tan',3,4), ('Shift',4,4),
            ('log',1,5), ('ln',2,5), ('^',3,5), ('!',4,5),
            ('π',5,0), ('e',5,1), ('(',5,2), (')',5,3),
            ('Quad',5,4), ('Cubic',5,5)
        ]

        for (text, r, c) in buttons:
            b = tk.Button(self.root, text=text, width=6, height=2, command=lambda t=text: self.click(t))
            b.grid(row=r, column=c)

    def click(self, key):
        if key == "=":
            try:
                expression = self.entry.get().replace('π', str(math.pi)).replace('e', str(math.e))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(eval(expression)))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif key == "Shift":
            self.shift_mode = not self.shift_mode
            # Shift 모드 기능 변경 가능 (예: sin ↔ asin)
        elif key == "!":
            try:
                val = int(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(math.factorial(val)))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif key == "Quad":
            # 예시: 1,0,-4 → solve_quadratic
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "a,b,c 입력 후 solve")
        elif key == "Cubic":
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "a,b,c,d 입력 후 solve")
        else:
            self.entry.insert(tk.END, key)

if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()