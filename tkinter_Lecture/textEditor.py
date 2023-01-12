import tkinter as tk
from tkinter.filedialog import askopenfilename


def open_file():
    filepath = askopenfilename(
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    if not filepath:
        return
    txt_edit.delete('1.0', tk.END)
    with open(filepath, mode='r', encoding='utf-8') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f'Text Editor - {filepath}')


window = tk.Tk()
window.title('Text Editor')
window.rowconfigure([0], minsize=100, weight=1)
window.columnconfigure([1], minsize=100, weight=1)

frm_buttons = tk.Frame(master=window, relief=tk.RAISED, bd=2)
frm_buttons.grid(row=0, column=0, sticky='ns')

btn_open = tk.Button(master=frm_buttons, text='OPEN', command=open_file)
btn_open.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
btn_save = tk.Button(master=frm_buttons, text='Save As')
btn_save.grid(row=1, column=0, padx=5, sticky='ew')

txt_edit = tk.Text(master=window)
txt_edit.grid(row=0, column=1, sticky='nsew')

window.mainloop()
