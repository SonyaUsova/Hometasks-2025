import math
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max_sides = (max(one), max(two), max(three))
min_sides = (min(one), min(two), min(three))

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

area_max = triangle_area(*max_sides)
area_min = triangle_area(*min_sides)


print(f"Площадь треугольника с максимальными сторонами {max_sides}: {area_max:.2f}")
print(f"Площадь треугольника с минимальными сторонами {min_sides}: {area_min:.2f}")
print()