from random import *
s = [randint(0, 10) for _ in range(10)]
print(s)
a = []
for i in s:
    if i % 2 != 0:
        a.append(i)
if len(a) == 0:
    print('таких чисел нет ')

print(sorted(a, reverse=True))
