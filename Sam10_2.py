class EmptyFileException(Exception):
    pass

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        if not content:
            raise EmptyFileException("файл пустой")
        print(content)

if __name__ == '__main__':
    # Для показа - создайте два файла: empty.txt и not_empty.txt
    filenames = ['empty.txt', 'not_empty.txt']
    for f in filenames:
        try:
            read_file(f)
        except EmptyFileException as e:
            print(e)
