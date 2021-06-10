import sys

while True:
    try:
        x = int(input("Number"))
        y = int(input("Divide by"))
        ans = x / y
        print(ans)
        break
    except:
        print(sys.exc_info()[0])
        print()
