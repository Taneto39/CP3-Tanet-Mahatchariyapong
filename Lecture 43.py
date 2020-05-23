ans = 30
inputAns = int(input("Guess Number>>"))
while not inputAns == ans:
    inputAns = int(input("Guess Number>>"))
    if ans > inputAns:
        print("Answer is more.")
    elif ans < inputAns:
        print("Answer is less.")
    else:
        print("Congratulations!!")
print("Answer is", ans)
