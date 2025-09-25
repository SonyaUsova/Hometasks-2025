numbers = [1, 499, 3,4 ,6,8,9, 1342]
value = int (input("Введите значение  переменной: "))
if value in numbers:
    if value %2==0:
        print("Переменная четная и есть в массиве numbers")
    else:
        print("Переменная нечетная и есть в массиве numbers")
else:
    print(f"Переменной не в массиве numbers и она равна {value}")
