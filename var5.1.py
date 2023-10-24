from random import *
s = [randint(-10,10) for i in range(10)]
for i in range (9):
    if s[i]<0 and s[i+1]<0:

        print(s[i], s[i+1])
print(s)
