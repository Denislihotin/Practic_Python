from random import*
n = int(input('введите чсисло '))
a = [[randint(1,15)for i in range(n)]for j in range(n)]
print(a)
for i in range(n):
    j = n-1
    j1 = 0
    a[i][j],a[i][j1] = a[i][j1],a[i][j]
for row in a:
    print(row)
