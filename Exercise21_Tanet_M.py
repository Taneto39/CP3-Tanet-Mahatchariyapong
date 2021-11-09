from tkinter import *

def calculateBMI(event):
    result = float(textboxWeight.get()) / (((float(textboxHeight.get())) / 100) ** 2)
    if result >= 30.0:
        text2configure = "คุณอ้วนมากเกินไป BMI = "+str(result)
    elif result >= 25.0:
        text2configure = "คุณอ้วนเกินไป BMI = "+str(result)
    elif result >= 23.0:
        text2configure = "คุณมีน้ำหนักเกิน BMI = "+str(result)
    elif result >= 18.6:
        text2configure = "น้ำหนักคุณปกติ BMI = "+str(result)
    else:
        text2configure = "คุณผอมเกินไป BMI = "+str(result)
    labelResultBMI.configure(text=text2configure)

mainWindow = Tk()
labelWeight = Label(mainWindow, text="น้ำหนักตัว (Kg.)")
labelWeight.grid(row=0, column=0)
textboxWeight = Entry(mainWindow)
textboxWeight.grid(row=0, column=1)
labelHeight = Label(mainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=1, column=0)
textboxHeight = Entry(mainWindow)
textboxHeight.grid(row=1, column=1)
buttonCal = Button(mainWindow, text="คำนวณ")
buttonCal.bind('<Button-1>', calculateBMI)
buttonCal.grid(row=2, column=0)
labelResultBMI = Label(mainWindow, text="ผลลัพธ์")
labelResultBMI.grid(row=2, column=1)

mainWindow.mainloop()
