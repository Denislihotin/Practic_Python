n = 3
a = []
for i in range(n):
    b = []
    for j in range(n):
        print('введите ',i,',',j,' элемент ')
        b.append(int(input()))
    a.append(b)
summ = sum(a[0])
def mat(a):
    for i in range(len(a)):
        s = 0
        for j in range(len(a)):
            s += a[j][i]
        if s != summ or summ != s:
            return "false"
    return "true"
print(mat(a))
print(a)

