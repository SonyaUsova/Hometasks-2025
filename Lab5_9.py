def superset (set_1, set_2):
    if set_1>set_2:
        print(f'Объект {set_1} является чистым супермножеством')
    elif set_1==set_2:
        print(f'Множества равны')
    elif set_1<set_2:
        print(f'Объект {set_2} является чистым супермножеством')
    else:
        print(f'Суперножества не обнаружено')

if __name__ == '__main__':
    superset({1,2,3,5}, {3,5})
    superset({1, 2, 3, 5}, {5,3,2,1})
    superset({3,5}, {5,3,2,1})
    superset({90, 100}, {3,5})