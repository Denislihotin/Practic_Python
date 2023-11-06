def kvadrat():
    a = int(input('введите сторону кавадрата '))
    print(a**2)
def krug():
    r = int(input('введите радиус круга '))
    print(3.14*r**2)
def treygolnik():
    a = int(input('введите сторону треугоьника '))
    h = int(input('введите высоту треугольника '))
    print(0.5*(a*h))
a = input('введите название фигуры ')
if a == 'квадрат':
    print(kvadrat())
elif a == 'круг':
    print(krug())
elif a == 'треугольник':
    print(treygolnik())
else:
    print('введите другую фигуру ')



