from random import*
s = [randint(1,20) for i in range(8)]
d = []
for i in range(len(s)):
    if s[i]<15:
        d.append((s[i])*2)
print(s)
print(d)