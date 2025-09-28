num = input()
num = float(num) if num.replace('.', '', 1).isdigit() else None
if num is None or not (0 <= num <= 10):
    print("Некорректный ввод")
else:
    if 0 <= num <= 3:
        print("от 0 до 3 включительно")
    elif 3 < num < 6:
        print("от 3 до 6")
    else:
        print("от 6 до 10 включительно")