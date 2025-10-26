with open('input.txt', 'a+') as f:
    f.write('\nНе уходи, постой, фанатка!')
    f.seek(0)
    result = f.readlines()
    print(result)


