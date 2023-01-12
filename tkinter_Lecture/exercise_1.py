import tkinter as tk

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure([0, 1], weight=1)
root.title('Address Entry Form')

frame1 = tk.Frame(master=root, relief=tk.SUNKEN, borderwidth=3)
frame2 = tk.Frame(master=root)
frame1.pack()
frame2.pack()
frame1.columnconfigure([0, 1], weight=1)
frame1.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)
frame2.columnconfigure(0, weight=1)
frame2.rowconfigure([0, 1], weight=1)

label = ['First Name:',
         'Last Name:',
         'Address Line 1:',
         'Address Line 2:',
         'City:',
         'State/Province:',
         'Postal Code:',
         'Country:']
for idx, text in enumerate(label):
    label_txt = tk.Label(master=frame1, width=11, text=text, anchor='e')
    label_txt.grid(row=idx, column=0)
    entry = tk.Entry(master=frame1, width=50)
    entry.grid(row=idx, column=1)

button1 = tk.Button(text='Submit', relief=tk.RAISED, borderwidth=3, padx=10)
button2 = tk.Button(text='Clear', relief=tk.RAISED, borderwidth=3, padx=10)
button1.pack(side=tk.RIGHT, padx=5, pady=5)
button2.pack(side=tk.RIGHT, padx=5, pady=5)

root.mainloop()
