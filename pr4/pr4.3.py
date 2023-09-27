a = int(input(""))
b = int(input(""))
if a<b:
    print("число a должно быть больше чем b")
else:
    if a%2==1:
        for c in range(a,b-1,-2):
            print(c, end=", ")
    else:
        for c in range(a-1,b-1,-2):
            print(c, end=", ")



