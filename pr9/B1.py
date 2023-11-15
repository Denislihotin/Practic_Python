a = []
n = 1
m = int(input('введите количесство ссторк: '))
for i in range(m):
    b=[]
    for j in range(n):
        print('введите[',i,',',j,'] элемент ')
        b.append(int(input()))
    a.append(b)
def maximum():
    max = 0
    for i in range(m):
        for j in range(n):
            if a[i][j]>max:
                max = a[i][j]
    return max
print(maximum())
print(a)
