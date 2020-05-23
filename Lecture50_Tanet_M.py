def plusNumber(x, y):
    print(x + y)
def minusNumber(x, y):
    print(x - y)
def multiNumber(x, y):
    print(x * y)
def devideNumber(x, y):
    print(x / y)
def processNumber(x, y):
    print("X + Y =", end="")
    plusNumber(x, y)
    print("X - Y =", end="")
    minusNumber(x, y)
    print("X * Y =", end="")
    multiNumber(x, y)
    print("X / Y =", end="")
    devideNumber(x, y)
processNumber(int(input("X = ")), int(input("Y = ")))
