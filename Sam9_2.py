class Tomato:
    # Статическое свойство states содержит все стадии созревания помидора
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        # Динамические свойства:
        # _index — индекс помидора (уникальный для каждого объекта)
        # _state — текущая стадия созревания (начинается со стадии отсутствует)
        self._index = index
        self._state = 0

    def grow(self):
        # Переводит томат на следующую стадию созревания, пока не достигнут максимальный этап
        if self._state < max(Tomato.states.keys()):
            self._state += 1

    def is_ripe(self):
        # Проверяет, созрел ли томат (стадия 'красный')
        return self._state == max(Tomato.states.keys())

    def get_state(self):
        # Возвращает текущую стадию созревания текстом
        return Tomato.states[self._state]


class TomatoBush:
    def __init__(self, count):
        # Динамическое свойство tomatoes — список из count помидоров (объектов Tomato)
        self.tomatoes = [Tomato(index) for index in range(1, count + 1)]

    def grow_all(self):
        # Переводит все помидоры в списке на следующую стадию созревания
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Проверяет, что все помидоры созрели
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        # Очищает список помидоров после сбора урожая
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        # Динамические свойства:
        # name — публичное свойство с именем садовника
        # _plant — приватное свойство с растением (объект класса TomatoBush)
        self.name = name
        self._plant = plant

    def work(self):
        # Садовник ухаживает за растением, вызывая его рост
        print(f'Садовник {self.name} ухаживает за растением...')
        self._plant.grow_all()

    def harvest(self):
        # Пробует собрать урожай, если все помидоры созрели
        if self._plant.all_are_ripe():
            print('Все помидоры созрели! Садовник собирает урожай.')
            self._plant.give_away_all()
        else:
            print('Помидоры еще не созрели. Нужно продолжать ухаживать.')

    @staticmethod
    def knowledge_base():
        # Выводит справку по садоводству
        print('''
        Справка по садоводству:
        1. Садовник ухаживает за растением, заставляя его расти.
        2. Томаты проходят стадии созревания: отсутствует, цветение, зеленый, красный.
        3. Растение можно собирать, только когда все томаты созрели.
        ''')


# Тестирование работы программы

# Создание куста с 3 томатами и садовника с именем Иван
bush = TomatoBush(3)
gardener = Gardener('Иван', bush)

