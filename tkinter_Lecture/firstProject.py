import tkinter as tk
from tkinter import ttk
from currency_converter import CurrencyConverter
# from datetime import date
import re


def check_num(new_val):
    return re.match('^[0-9]*$', new_val) is not None and len(new_val) <= 10


def alternate_currency():
    # result_var.set('35')
    input_cur = lbox_input_currency.get()
    output_cur = lbox_output_currency.get()
    lbox_input_currency.set(output_cur)
    lbox_output_currency.set(input_cur)
    input_value = ent_input_value.get()
    output_value = result_var.get()
    ent_input_value.delete(0, tk.END)
    ent_input_value.insert(0, output_value)
    result_var.set(input_value)


def convert():
    pass


# provide list of currencies
c = CurrencyConverter()
lst_currency = list(c.currencies)
lst_currency.sort()

window = tk.Tk()
window.rowconfigure([0], minsize=100)
# window.rowconfigure([1], minsize=50)
window.columnconfigure([0], minsize=210)
window.resizable(False, False)
check_num_wrapper = (window.register(check_num), '%P')

frm_program = tk.Frame(window, borderwidth=1, relief=tk.RAISED)
frm_program.rowconfigure([0, 1], minsize=50)
frm_program.columnconfigure([0, 1, 2], minsize=100)
frm_program.grid(row=0, column=0, sticky='nsew')

# first row widget
input_currency_var = tk.StringVar()
lbox_input_currency = ttk.Combobox(
    frm_program,
    textvariable=input_currency_var,
    values=lst_currency,
    state='readonly',
    width=10,
    font=40)
lbox_input_currency.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

btn_alt_currency = tk.Button(frm_program, text='\u21c4', command=alternate_currency)
btn_alt_currency.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

output_var = tk.StringVar()
lbox_output_currency = ttk.Combobox(
    frm_program,
    textvariable=output_var,
    values=lst_currency,
    state='readonly',
    width=10,
    font=40)
lbox_output_currency.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')

# second row widget
input_var = tk.StringVar()
ent_input_value = tk.Entry(
    frm_program,
    textvariable=input_var,
    validate='key',
    validatecommand=check_num_wrapper,
    width=10,
    font=40)
ent_input_value.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
ent_input_value.bind()

lbl_equal = tk.Label(frm_program, text=':', font=40)
lbl_equal.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

result_var = tk.StringVar()
lbl_result = tk.Label(frm_program,
                      textvariable=result_var,
                      bg='yellow',
                      font=40)
lbl_result.grid(row=1, column=2, padx=5, pady=5, sticky='nsew')

window.mainloop()
