import tkinter as tk
from tkinter import ttk
from currency_converter import CurrencyConverter
import re


# Entry can type only digits
def check_num(new_val):
    return re.match('^[0-9]*$', new_val) is not None and len(new_val) <= 10


# callback for alternate button
def alternate_currency():
    # alternate currency in combobox
    input_cur = cbx_input_currency.get()
    output_cur = cbx_output_currency.get()
    cbx_input_currency.set(output_cur)
    cbx_output_currency.set(input_cur)
    # clear value for prevent misunderstand
    ent_input_value.delete(0, tk.END)
    lbl_result['text'] = ''


# clear value for prevent misunderstand
def clear_value(e):
    ent_input_value.delete(0, tk.END)
    lbl_result['text'] = ''


# callback when user press enter
def convert(e):
    input_value = float(ent_input_value.get())
    result = c.convert(input_value, cbx_input_currency.get(), cbx_output_currency.get())
    lbl_result['text'] = round(result, 2)


# provide list of currencies
c = CurrencyConverter(fallback_on_wrong_date=True)
lst_currency = list(c.currencies)
lst_currency.sort()

window = tk.Tk()
window.rowconfigure([0], minsize=100)
window.columnconfigure([0], minsize=210)
window.resizable(False, False)
check_num_wrapper = (window.register(check_num), '%P')
window.title('Simple Currency Converter')

frm_program = tk.Frame(window, borderwidth=1, relief=tk.RAISED)
frm_program.rowconfigure([0, 1], minsize=50)
frm_program.columnconfigure([0, 1, 2], minsize=100)
frm_program.grid(row=0, column=0, sticky='nsew')

# first row widget
input_currency_var = tk.StringVar()
cbx_input_currency = ttk.Combobox(
    frm_program,
    textvariable=input_currency_var,
    values=lst_currency,
    state='readonly',
    width=10,
    font=40)
cbx_input_currency.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
cbx_input_currency.bind('<<ComboboxSelected>>', clear_value)

btn_alt_currency = tk.Button(frm_program, text='\u21c4', command=alternate_currency)
btn_alt_currency.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

output_var = tk.StringVar()
cbx_output_currency = ttk.Combobox(
    frm_program,
    textvariable=output_var,
    values=lst_currency,
    state='readonly',
    width=10,
    font=40)
cbx_output_currency.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')
cbx_output_currency.bind('<<ComboboxSelected>>', clear_value)

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
ent_input_value.bind('<KeyPress-Return>', convert)

lbl_equal = tk.Label(frm_program, text=':', font=40)
lbl_equal.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

lbl_result = tk.Label(frm_program,
                      text='',
                      font=40)
lbl_result.grid(row=1, column=2, padx=5, pady=5, sticky='nsew')

window.mainloop()
