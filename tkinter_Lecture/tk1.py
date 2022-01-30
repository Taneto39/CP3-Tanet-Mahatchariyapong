from tkinter import *
from datetime import datetime


def record_trans(menu_item):
    with open("sales.csv", mode='a', newline='', encoding='UTF-8') as f:
        price = menus[menu_item]
        dt = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        f.write(f'{menu_item},{price},{dt}\n')


def left_click(e):
    menu_item = e.widget.cget("text")
    # print(f'{menu_item} = {menus[menu_item]} Baht')
    tv_menu.set(f'{menu_item} = {menus[menu_item]} Baht')
    record_trans(menu_item)


menus = dict(mocha=30, latte=40, espresso=50,
             green_tea=25, tea=20, Thai_tea=30,
             coke=20, water=15, กาแฟดำ=25,
             ชาดำเย็น=30)
item_per_row = 2
main_window = Tk()
tv_menu = StringVar()
main_window.option_add("*font", "impact 25")
for idx, name in enumerate(menus.keys()):
    btn = Button(main_window, text=name, width=15)
    btn.grid(row=idx // item_per_row, column=idx % item_per_row)
    btn.bind("<Button-1>", left_click)
Label(main_window, text="menu", textvariable=tv_menu).grid(columnspan=item_per_row)
main_window.mainloop()
