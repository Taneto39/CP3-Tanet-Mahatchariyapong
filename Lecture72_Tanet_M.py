menuList = []
totalPrice = 0

def showbill():
    print("My Food".center(21, "="))
    for i in range(len(menuList)):
        print(menuList[i][0], menuList[i][1], "THB")
        global totalPrice
        totalPrice += menuList[i][1]

while True:
    menuName = input("Enter menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append([menuName, menuPrice])

showbill()
print(totalPrice, "THB in total.")
