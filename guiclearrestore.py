from breezypythongui import EasyFrame

class DemoGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="GUI Demo")

        self.label = self.addLabel(text="Python GUI Demo", row=0, column=0, columnspan=2)

        self.clearBtn = self.addButton(text="Clear", row=1, column=0, command=self.clearLabel)
        self.restoreBtn = self.addButton(text="Restore", row=1, column=1, command=self.restoreLabel)

        self.restoreBtn["state"] = "disabled"

    def clearLabel(self):
        self.label["text"] = ""
        self.clearBtn["state"] = "disabled"
        self.restoreBtn["state"] = "normal"

    def restoreLabel(self):
        self.label["text"] = "Python GUI Demo"
        self.restoreBtn["state"] = "disabled"
        self.clearBtn["state"] = "normal"

DemoGUI().mainloop()