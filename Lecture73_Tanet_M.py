dictMenuList = {"Apple": 5, "Grapes": 20, "Orange": 40}
menuList = []
valueList = []
totalPrice = 0


def showbill():
    print("My Food".center(21, "="))
    for i in range(len(menuList)):
        print(valueList[i], menuList[i][0]+"(s)", menuList[i][1], "THB")
        global totalPrice
        totalPrice += menuList[i][1]

while True:
    menuName = input("Enter menu : ").capitalize()
    if menuName.lower() == "exit":
        break
    elif menuName not in dictMenuList:
        print("We don't have that menu.", end=" ")
        print("(", end="")
        a = 1
        for i in dictMenuList.keys():#print list of menuName
            if a != len(dictMenuList.keys()):
                print(i, end=", ")
            else:
                print(i+")")
            a += 1
    else:
        global value
        value = int(input("How many "+menuName.capitalize()+" do you want?"))
        menuList.append([menuName, (dictMenuList[menuName])*value])
        valueList.append(value)

showbill()
print(totalPrice, "THB in total.")
