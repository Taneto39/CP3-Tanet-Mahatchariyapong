listOrderprice = []

def showBill():
    x = 0
    print("Food".center(10, "-"))
    for i in range(len(listOrderprice)):
        print(listOrderprice[i][0], listOrderprice[i][1])
        x += listOrderprice[i][1]
    print("Total is", x, "THB, Please.")

while True:
    nameFood = input("What would you like?(Type 'Exit' if you done.)")
    list = []
    if nameFood.capitalize() != "Exit":
        list.append(nameFood)
        list.append(int(input("How much is "+nameFood+"?")))
        listOrderprice.append(list)
    else:
        break

showBill()