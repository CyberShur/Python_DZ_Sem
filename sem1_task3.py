'''
Найти расстояние между двумя точками пространства
'''
from cmath import sqrt

xA = int(input("Введите координату {x} точки {A}: "))
yA = int(input("Введите координату {y} точки {A}: "))
zA = int(input("Введите координату {z} точки {A}: "))
xB = int(input("Введите координату {x} точки {B}: "))
yB = int(input("Введите координату {y} точки {B}: "))
zB = int(input("Введите координату {z} точки {B}: "))

print()
print(f"Введённые координаты: ({xA}, {yA}, {zA}) ({xB}, {yB}, {zB})")

diffX = xB - xA
diffY = yB - yA
diffZ = zB - zA

resultS = diffX**2 + diffY**2 + diffZ**2

result0 = sqrt(resultS)

print()
print(f"Расстояние между точками равно - {result0}")
