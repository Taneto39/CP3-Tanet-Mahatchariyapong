a = int(input())
b = 1
for i in range(a):
    b += 1
    c = a
    for j in range(b):
        text = (" "*c)+("*"*(j*2+1))
        c -= 1
        print(text)
print(" "*a+"|")
print("="*a+"V"+"="*a)
