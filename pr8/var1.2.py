from random import *
n = int(input())
B = [[randint(0,10)for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        print(B[i][j], end=' ')
    print()
for i, row in enumerate(B):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
for i in range(n):
    for j in range(n):
        print(B[i][j], end=' ')
    print()
