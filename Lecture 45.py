inputRound = int(input("How many round would you like?>>"))
sum = 0
for i in range(inputRound):
    sum += int(input("X"+str(i+1)+":"))
print("Sum =", sum)
