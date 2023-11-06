from random import *
s = [randint(1,10) for i in range(12)]
a = [randint(1,10) for i in range(12)]
b = [randint(1,10) for i in range(12)]
def f():
    k = 0
    for i in range(len(s)):
        k+=s[i]
        print(k, k/len(s))
def g():
    k = 0
    for i in range(len(a)):
        k+=a[i]
        print(k, k/len(a))
def h():
    k = 0
    for i in range(len(b)):
        k+=b[i]
        print(k, k/len(b))
print(s, a, b)
print(f(), g(), h())