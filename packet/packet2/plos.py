def krug(r):
    from math import pi
    print(f"Площадь круга с радиусом {r} равна",r*r*pi)
def qvad(x,y):
    print(f"Площадь четырехугольника со сторонами {x,y} равна", x*y)
def tres(x,y,z):
    try:
        p=(x+y+z)/2
        print(f"Площадь треугольника со сторонами {x,y,z} равна ",(p*(p-x)*(p-y)*(p-z))**0.5)
    except TypeError:
        print('Проверьте, правильно ли введены данные')

