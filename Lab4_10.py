from random import triangular

global result


def rectangle():
    a = float (input("Ширина:"))
    b = float (input("Высота:"))
    global result
    result = a*b


def tiangle():
    a = float(input("Основание:"))
    h = float(input("Высота:"))
    global result
    result = 0.5*a * h

figure = input("1-прямоугольник, 2-треугольник: ")
if figure  =='1':
    rectangle()
elif figure =='2':
    tiangle()

print (f"Площадь: {result}")