userName = input("Username : ")
passWord = input("Password : ")
product_01 = "Apple"
priceProduct_01 = 5
product_02 = "Orange"
priceProduct_02 = 10
product_03 = "Grape"
priceProduct_03 = 40
product_04 = "Melon"
priceProduct_04 = 100
if userName == "python" and passWord == "2020":
    print("----Welcome----")
    print("1.", product_01, priceProduct_01, "THB")
    print("2.", product_02, priceProduct_02, "THB")
    print("3.", product_03, priceProduct_03, "THB")
    print("4.", product_04, priceProduct_04, "THB")
    productInput = int(input("Choose product >>"))
    if productInput >= 1 and productInput <= 4:#check เลือกได้แค่1-4เท่านั้น
        if productInput == 1:
            curProduct = product_01#cur=current
            curProductPrice = priceProduct_01
        elif productInput == 2:
            curProduct = product_02
            curProductPrice = priceProduct_02
        elif productInput == 3:
            curProduct = product_03
            curProductPrice = priceProduct_03
        else:
            curProduct = product_04
            curProductPrice = priceProduct_04
    else:
        print("ERROR!!")
    curProductValue = int(input("How many "+curProduct+"?"))
    print("Order is", curProductValue, curProduct+"(s).")
    print(curProductPrice*curProductValue, "THB in total.")
else:
    print("Your Username or Password is wrong!!")