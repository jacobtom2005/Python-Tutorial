from breezypythongui import EasyFrame
from tkinter import messagebox

class BillingGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Billing System")

        self.addLabel(text="Item Price", row=0, column=0)
        self.priceField = self.addFloatField(value=0.0, row=0, column=1)

        self.addLabel(text="Quantity", row=1, column=0)
        self.qtyField = self.addIntegerField(value=0, row=1, column=1)

        self.addButton(text="Generate Bill", row=2, column=0, columnspan=2,
                       command=self.generateBill)

        self.addLabel(text="Final Amount", row=3, column=0)
        self.resultField = self.addFloatField(value=0.0, row=3, column=1, precision=2)
        self.resultField["state"] = "readonly"

    def generateBill(self):
        try:
            price = self.priceField.getNumber()
            qty = self.qtyField.getNumber()

            total = price * qty

            if total > 1000:
                total = total * 0.9

            self.resultField["state"] = "normal"
            self.resultField.setNumber(total)
            self.resultField["state"] = "readonly"

        except ValueError:
            messagebox.showerror("Error", "Enter valid input!")

BillingGUI().mainloop()