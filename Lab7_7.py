lines = ['лучшая!', 'гениальная', 'красивая']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nЯ-'+line)
    print('Done!')
