class SiteChecker:
    def __init__(self, func):
        print('> Класс SiteChecker метод __init__ условный запуск')
        self.func = func

    def __call__(self):
        print('> Проверка перед запуском', self.func.__name__)
        self.func()
        print('> Проверка безопасности включена')


@SiteChecker
def site():
    print("Усердная работа сайта")

if __name__=='__main__':
    print('>> Сайт запущен')
    site()  # Здесь вызовется метод __call__ объекта-декоратора SiteChecker
    print('>> Сайт выключен')
