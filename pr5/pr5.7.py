s = str(input("введите строку "))
(s.count('п'))
s = s.replace ('п', '*', s.count('п') // 2)
print(s)
