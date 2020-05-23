def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("Welcome!")
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    global returnMenuselect
    returnMenuselect = int(input(">>"))
def vatCal(Totalprize, Taxrate):
    return Totalprize*(1+(Taxrate/100))
def totalCal():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCal(price1+price2, int(input("TAX rate : ")))

while not login():#ตรวจสอบชื่อและรหัสผ่าน
    print("Username or Password is wrong.")
showMenu()
menuSelect()
while returnMenuselect != 1 and returnMenuselect != 2:#ตรวจสอบว่าผู้ใช้กรอกเลขที่ถูกต้อง
    print("Error! We have just 2 menu.(1, 2)")
    menuSelect()
if returnMenuselect == 1:
    print("Total =", vatCal(int(input("Prize(THB) : ")), int(input("TAX rate : "))))
else:
    print("Total =", totalCal())
