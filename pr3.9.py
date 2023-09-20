a = int(input("введите число"))
b = int(input("введите число"))
c = int(input("введите число"))
if a+b>c and b+c>a and a+c>b:
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**(1/2)
    print("{0:.4f}".format(s))
else:
    print("числа не являются сторонами треугольника")