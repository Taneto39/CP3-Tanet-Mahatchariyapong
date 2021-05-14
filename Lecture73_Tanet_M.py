dictMenuList = {"Apple": 5, "Grapes": 20, "Orange": 40}
menuListprice = []

def showbill():
    print("My Food".center(21, "="))
    totalPrice = 0
    for i in range(len(menuListprice)):
        print("%d %s(s) %d %d THB" % (menuListprice[i][0], menuListprice[i][1], dictMenuList.get(menuListprice[i][1]), menuListprice[i][2]))
        totalPrice += menuListprice[i][2]
    print(totalPrice, "THB in total.")

while True:
    menuName = input("Enter menu : ").capitalize()
    if menuName.lower() == "exit":
        break
    elif menuName not in dictMenuList:
        print("We don't have that menu.")
    else:
        value = int(input("How many "+menuName.capitalize()+" do you want?"))
        menuListprice.append([value, menuName, (dictMenuList[menuName])*value])

showbill()