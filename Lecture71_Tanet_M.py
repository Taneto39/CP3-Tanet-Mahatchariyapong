menuList = []
priceList = []
totalPrice = 0

def showbill():
    print("My Food".center(21, "="))
    for i in range(len(menuList)):
        print(menuList[i], priceList[i], "THB")
        global totalPrice
        totalPrice += priceList[i]

while True:
    menuName = input("Enter menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showbill()
print(totalPrice, "THB in total.")
