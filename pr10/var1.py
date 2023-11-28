f = open('LihotinDenis_UB-31_vvod.txt','r')
a = []
for row in f:
    row = [int(num) for num in row.split()]
    a.append(row)
print(a)
n=3
k=0
s=0
for i in range(n):
    for j in range(n):
        if i < j and a[i][j]>0:
            s+=a[i][j]
            k+=1
f.close()
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
import sys
print('сумма элементов',s, 'количество элементов',k)
original_stdout = sys.stdout
with open('LihotinDenis_UB-31_vivod.txt','w') as f:
    sys.stdout = f
    print('summa elem', s, 'kol-vo elem', k)
    sys.stdout = original_stdout




