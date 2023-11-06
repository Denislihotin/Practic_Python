n=3
k=0
s=0
a = []
for i in range(n):
    b=[]
    for j in range(n):
        print('введите[',i,',',j,'] элемент ')
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(n):
        if i < j and a[i][j]>0:
            s+=a[i][j]
            k+=1
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
print('сумма элементов',s, 'количество элементов',k)




