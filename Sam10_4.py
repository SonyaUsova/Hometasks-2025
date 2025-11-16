class LoggerDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Вызвана функция: {self.func.__name__}, аргументы: {args}")
        result = self.func(*args, **kwargs)
        print(f"Работа {self.func.__name__} завершена\n")
        return result


@LoggerDecorator
def greet(name):
    print(f"Привет, {name}!")


@LoggerDecorator
def square(x):
    print(f"{x}^2 = {x * x}")


if __name__ == '__main__':
    greet('Вовочка')
    square(5)
