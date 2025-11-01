class Shape:
    # Базовый класс для фигур, определяет интерфейс area
    def area(self):
        # Метод area должен быть переопределён в наследниках
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        # Инициализируем прямоугольник с шириной и высотой
        self.width = width
        self.height = height

    def area(self):
        # Вычисляем площадь прямоугольника
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        # Инициализируем круг с радиусом
        self.radius = radius

    def area(self):
        # Вычисляем площадь круга (приблизительно)
        return 3.14 * self.radius * self.radius

# Создание экземпляров прямоугольника и круга с задаными параметрами
rect = Rectangle(5, 10)
circle = Circle(3)

# Вывод площади фигуры
print("Rectangle area:", rect.area())
print("Circle area:", circle.area())
