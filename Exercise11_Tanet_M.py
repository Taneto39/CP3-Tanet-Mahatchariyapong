heightPyramid = int(input())
for i in range(heightPyramid):
    text = (" "*(heightPyramid-1))+("*"*(i*2+1))
    heightPyramid -= 1
    print(text)
