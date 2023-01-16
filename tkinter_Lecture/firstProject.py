import tkinter as tk
from tkinter import ttk
from currency_converter import CurrencyConverter
from datetime import date


def test():
    pass


# provide list of currencies
c = CurrencyConverter()
lst_currency = list(c.currencies)
lst_currency.sort()

window = tk.Tk()
window.rowconfigure([0], minsize=100)
window.rowconfigure([1], minsize=50)
window.columnconfigure([0], minsize=210)
window.resizable(False, False)

frm_program = tk.Frame(window, borderwidth=1, relief=tk.RAISED)
frm_program.rowconfigure([0, 1], minsize=50)
frm_program.columnconfigure([0, 1, 2], minsize=100)
frm_program.grid(row=0, column=0, sticky='nsew')

# first row widget
input_currency_var = tk.StringVar()
lbox_input_currency = ttk.Combobox(frm_program, textvariable=input_currency_var, values=lst_currency, state='readonly')
lbox_input_currency.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

btn_alt_currency = tk.Button(frm_program, text='\u21c4')
btn_alt_currency.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

output_currency_var = tk.StringVar()
lbox_output_currency = ttk.Combobox(
    frm_program,
    textvariable=output_currency_var,
    values=lst_currency,
    state='readonly')
lbox_output_currency.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')

# second row widget
ent_input_value = tk.Entry(frm_program, )

window.mainloop()
