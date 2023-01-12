import tkinter as tk

window = tk.Tk()
window.title('Temperature Converter')
window.resizable(width=False, height=False)


def convert():
    temp_f = float(ent_temp.get())
    lbl_result['text'] = f'{round((((temp_f - 32) * 5) / 9), 2)} \N{DEGREE CELSIUS}'


frm_entry = tk.Frame(master=window)
frm_entry.grid(row=0, column=0, padx=10)

ent_temp = tk.Entry(master=frm_entry, width=10)
ent_temp.grid(row=0, column=0, sticky='e')
# ent_temp.bind(event=)

tk.Label(master=frm_entry, text='\N{DEGREE FAHRENHEIT}').grid(row=0, column=1, sticky='w')

btn_convert = tk.Button(text='\N{RIGHTWARDS BLACK ARROW}', command=convert)
btn_convert.grid(row=0, column=2, pady=10)

lbl_result = tk.Label(text='-- \N{DEGREE CELSIUS}')
lbl_result.grid(row=0, column=3, padx=10)

window.mainloop()
