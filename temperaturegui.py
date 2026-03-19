from breezypythongui import EasyFrame
from tkinter import messagebox

class TempConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")

        self.addLabel(text="Celsius", row=0, column=0)
        self.celsiusField = self.addFloatField(value=0.0, row=0, column=1)

        self.convertBtn = self.addButton(text="Convert to Fahrenheit",
                                         row=1, column=0, columnspan=2,
                                         command=self.convert)

        self.addLabel(text="Fahrenheit", row=2, column=0)
        self.fahrenheitField = self.addFloatField(value=0.0, row=2, column=1, precision=2)
        self.fahrenheitField["state"] = "readonly"

    def convert(self):
        try:
            celsius = float(self.celsiusField.getNumber())
            fahrenheit = (celsius * 9/5) + 32

            self.fahrenheitField["state"] = "normal"
            self.fahrenheitField.setNumber(fahrenheit)
            self.fahrenheitField["state"] = "readonly"

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number!")

# Run the application
TempConverter().mainloop()