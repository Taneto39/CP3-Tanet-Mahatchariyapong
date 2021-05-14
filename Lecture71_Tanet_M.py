listOrder = []
listPrice = []

def showBill():
    x = 0
    print("Food".center(10, "-"))
    for i in range(len(listOrder)):
        print(listOrder[i], listPrice[i])
        x += listPrice[i]
    print("Total is", x, "THB, Please.")

while True:
    x = input("What would you like?(Type 'Exit' if you done.)")
    if x.capitalize() != "Exit":
        listOrder.append(x.capitalize())
        listPrice.append(int(input("How much is "+x+"?")))
    else:
        break

showBill()