from tkinter import *

root = Tk()
currency = [str(i) for i in range(10, 22)]
primary_currency = ""
secondary_currency = []


def pri_choose():
    global primary_currency
    primary_currency = currency[pri_cur.get()]
    currency.remove(primary_currency)
    show_sec_cur()


def show_sec_cur():
    for i in range(12):
        globals()[f'rBtn{i}'].destroy()
    btn_pri_receive.configure(text='plot', command=save_sec_cur)
    Label(root, text=f'{primary_currency}').grid(row=3, column=2)
    for index, ele in enumerate(currency):
        globals()[f'check{index}'] = IntVar()
        Checkbutton(root, text=currency[index], variable=globals()[f'check{index}']).grid(row=index // 4,
                                                                                          column=index % 4)


def save_sec_cur():
    global secondary_currency
    for i in range(11):
        secondary_currency.append(globals()[f'check{i}'].get())
    index_cur = secondary_currency.copy()
    secondary_currency.clear()
    for index, value in enumerate(index_cur):
        if value == 1:
            secondary_currency.append(currency[index])
    time_get()


def time_get():
    pass


pri_cur = IntVar()
for idx, cur in enumerate(currency):
    globals()[f'rBtn{idx}'] = Radiobutton(root, text=cur, variable=pri_cur, value=idx)
    globals()[f'rBtn{idx}'].grid(row=idx // 4, column=idx % 4)
Label(root, text=f'Primary').grid(row=3, column=0)
Label(root, text=f'Currency').grid(row=3, column=1)
btn_pri_receive = Button(root, text="OK", command=pri_choose)
btn_pri_receive.grid(row=3, column=3)
root.mainloop()
