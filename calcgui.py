from breezypythongui import EasyFrame
from tkinter import messagebox

class CalculatorGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Simple Calculator")

        self.addLabel(text="Number 1", row=0, column=0)
        self.num1 = self.addIntegerField(value=0, row=0, column=1)

        self.addLabel(text="Number 2", row=1, column=0)
        self.num2 = self.addIntegerField(value=0, row=1, column=1)

        self.addButton(text="Add", row=2, column=0, command=self.add)
        self.addButton(text="Subtract", row=2, column=1, command=self.subtract)
        self.addButton(text="Multiply", row=3, column=0, command=self.multiply)
        self.addButton(text="Divide", row=3, column=1, command=self.divide)

        self.addLabel(text="Result", row=4, column=0)
        self.resultField = self.addFloatField(value=0.0, row=4, column=1, precision=2)
        self.resultField["state"] = "readonly"

    def getInputs(self):
        try:
            n1 = self.num1.getNumber()
            n2 = self.num2.getNumber()
            return n1, n2
        except ValueError:
            messagebox.showerror("Error", "Enter valid integers!")
            return None, None

    def displayResult(self, value):
        self.resultField["state"] = "normal"
        self.resultField.setNumber(value)
        self.resultField["state"] = "readonly"

    def add(self):
        n1, n2 = self.getInputs()
        if n1 is not None:
            self.displayResult(n1 + n2)

    def subtract(self):
        n1, n2 = self.getInputs()
        if n1 is not None:
            self.displayResult(n1 - n2)

    def multiply(self):
        n1, n2 = self.getInputs()
        if n1 is not None:
            self.displayResult(n1 * n2)

    def divide(self):
        try:
            n1, n2 = self.getInputs()
            if n1 is not None:
                result = n1 / n2
                self.displayResult(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")

CalculatorGUI().mainloop()