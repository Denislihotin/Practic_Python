from random import*
s = [randint(1,10) for i in range(15)]
k = 0
for i in range(len(s)):
    if i%2==0:
        k+=s[i]
print(s)
print(k)
