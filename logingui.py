from breezypythongui import EasyFrame
from tkinter import messagebox

class LoginGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Login Form")

        self.addLabel(text="Username", row=0, column=0)
        self.usernameField = self.addTextField("", row=0, column=1)

        self.addLabel(text="Password", row=1, column=0)
        self.passwordField = self.addTextField("", row=1, column=1)
        self.passwordField["show"] = "*" 

        self.addButton(text="Login", row=2, column=0, columnspan=2,
                       command=self.login)

        self.correct_username = "admin"
        self.correct_password = "1234"

    def login(self):
        username = self.usernameField.getText()
        password = self.passwordField.getText()

        if username == "" or password == "":
            messagebox.showerror("Error", "Username or Password cannot be empty!")

        elif username == self.correct_username and password == self.correct_password:
            messagebox.showinfo("Success", "Login Successful")

        else:
            messagebox.showerror("Error", "Invalid Username or Password")

LoginGUI().mainloop()