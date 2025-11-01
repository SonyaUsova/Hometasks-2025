class Car:
    # Инициализация экземпляра класса с маркой и моделью автомобиля
    def __init__(self, make, model):
        self.make = make  # Марка автомобиля
        self.model = model  # Модель автомобиля

# Создаем объект my_car с маркой Toyota и моделью Corolla
my_car = Car("Toyota", "Corolla")
