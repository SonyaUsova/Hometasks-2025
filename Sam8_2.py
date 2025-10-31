def add_expense():
    date = input("Дата (ДД.ММ.ГГГГ): ")
    amount = input("Сумма: ")
    category = input("Категория: ")
    desc = input("Описание: ")
    with open('expenses.txt', 'a', encoding='utf-8') as f:
        f.write(f'{date},{amount},{category},{desc}\n')
    print("Расход добавлен!")

def view_expenses():
    print("Все расходы:")
    with open('expenses.txt', 'r', encoding='utf-8') as f:
        print(f.read())

while True:
    cmd = input("1: Добавить\n2: Показать\n3: Выйти\nВыберите: ")
    if cmd == '1':
        add_expense()
    elif cmd == '2':
        view_expenses()
    else:
        break
