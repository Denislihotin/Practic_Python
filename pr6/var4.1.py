from random import*
s = [randint(0,100) for i in range(10)]
a = 0
k = 0
for i in range(len(s)):
    if s[i]>a:
        a = s[i]
        k = i+1

print(s, a, k)