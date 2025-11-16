def add_two_and_x():
    try:
        x = input("Введите число: ")
        result = 2 + int(x)
        print(f"Результат: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
    add_two_and_x()
    # Проверьте: вводите 4, "abc", 5.6
