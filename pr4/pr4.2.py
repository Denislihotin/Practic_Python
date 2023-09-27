a = int(input(""))
b = int(input(""))
if a>b:
    for c in range(b,a+1,1):
        print(c, end=",")
else:
    for c in range(a,b+1,1):
        print(c, end=",")


