class NegativeResultError(Exception):
    pass


def subtract(a, b):
    res = a - b
    if res < 0:
        raise NegativeResultError("Результат меньше нуля")
    print(f"Разность: {res}")


def parse_age(age):
    if int(age) < 0:
        raise NegativeResultError("Возраст не может быть отрицательным")
    print(f"Возраст: {age}")


if __name__ == '__main__':
    for x, y in [(10, 5), (3, 7)]:
        try:
            subtract(x, y)
        except NegativeResultError as e:
            print("Ошибка:", e)

    for age in ["20", "-2"]:
        try:
            parse_age(age)
        except NegativeResultError as e:
            print("Ошибка:", e)
