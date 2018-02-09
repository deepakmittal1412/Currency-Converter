from currency_converter import CurrencyConverter
from tkinter import *


def view():
    c = CurrencyConverter()
    try:
        con = c.convert(float(e3.get()), e1.get(), e2.get())
    except:
        con = "Invalid\nCurrency code or Amount"
    win2 = Toplevel()
    win2.title("Results")
    win2.resizable(0, 0)
    win2.propagate()
    win2.config(height=200, width=200)
    Label(win2, text=con, bg='seashell', fg='black', font=('Helvetica', 20, 'bold')).pack()
    win2.mainloop()


root = Tk()
root.title("Currency Converter")
root.resizable(0, 0)
root.propagate()
root.config(height=200, width=200, bg='seashell')
l1 = Label(root, text="From (Enter currency code) :", bg='seashell', fg='black', font=('Helvetica', 10, 'bold')).grid(
    row=0, column=0)
e1 = Entry(root)
e1.insert(0, '')
e1.grid(row=0, column=1)
l2 = Label(root, text="To (Enter currency code) :", bg='seashell', fg='black', font=('Helvetica', 10, 'bold')).grid(
    row=1, column=0)
e2 = Entry(root)
e2.insert(0, '')
e2.grid(row=1, column=1)
l3 = Label(root, text="Amount :", bg='seashell', fg='black', font=('Helvetica', 10, 'bold')).grid(row=2, column=0)
e3 = Entry(root)
e3.insert(0, '')
e3.grid(row=2, column=1)
b1 = Button(root, text="CONVERT", command=view, bg='peach puff', font=('Helvetica', 8, 'bold')).grid(row=3, column=1)
root.mainloop()
