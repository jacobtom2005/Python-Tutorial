from breezypythongui import EasyFrame
from tkinter import messagebox

class PasswordStrengthGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Password Strength Checker")

        self.addLabel(text="Password", row=0, column=0)
        self.passwordField = self.addTextField("", row=0, column=1)
        self.passwordField["show"] = "*"

        self.addButton(text="Check Strength", row=1, column=0, columnspan=2,
                       command=self.checkStrength)

        self.addLabel(text="Strength", row=2, column=0)
        self.outputField = self.addTextField("", row=2, column=1)
        self.outputField["state"] = "readonly"

    def checkStrength(self):
        password = self.passwordField.getText()

        if password == "":
            messagebox.showerror("Error", "Password cannot be empty!")
            return

        length = len(password) >= 8
        has_digit = any(char.isdigit() for char in password)
        has_special = any(not char.isalnum() for char in password)

        score = length + has_digit + has_special

        if score == 1:
            strength = "Weak"
        elif score == 2:
            strength = "Moderate"
        else:
            strength = "Strong"

        self.outputField["state"] = "normal"
        self.outputField.setText(strength)
        self.outputField["state"] = "readonly"

PasswordStrengthGUI().mainloop()