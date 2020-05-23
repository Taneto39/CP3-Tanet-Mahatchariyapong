roundValue = 3
while roundValue > 0:
    userName = input("Username :")
    passWord = input("Password :")
    if userName == "admin" and passWord == "1234":
        roundValue = 0
        print("Welcome!")
    else:
        roundValue -= 1
        if roundValue == 0:
            print("You are guess too much.")
        else:
            print("Username or Password is wrong.", roundValue, "remain(s).")

