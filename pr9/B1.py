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
    for i in range(m):
        for j in range(n):
            if a[i][j]<a[i+1][j]:
                return a[i+1][j]
print(maximum())
print(a)
