n=int(input(' '))
def q(n):
    for i in range(1, n):
        if n%i==0:
            result='NO'
            break
        else:
            result='YES'
    return(result)
if n<=1:
    print('n должно быть больше 1 ')
print(q(n))
