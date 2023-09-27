a = int(input('введите число а '))
b = int(input('введите число b '))
if a>b:
    print('a не должно быть больше b ')
else:
    for c in range(a,b+1):
        print(c, end="; ")
