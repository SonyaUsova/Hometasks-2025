import os

def print_docs(directory):
    for root, dirs, files in os.walk(directory):
        print(f'Папка: {root} содержит:')
        print(f'  Подпапки: {", ".join(dirs)}')
        print(f'  Файлы: {", ".join(files)}')
        print('-' * 40)

print_docs(r'/Users/sonusowa/Desktop/для уника всё')  # Укажите полный путь к вашей папке
