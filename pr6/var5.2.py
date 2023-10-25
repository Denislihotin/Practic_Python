from random import*
s = [randint (1, 20) for i in range (10)]
a = []
k = 0
for i in s:
    if i not in a:
        a.append (i)
print(s)
print(a)