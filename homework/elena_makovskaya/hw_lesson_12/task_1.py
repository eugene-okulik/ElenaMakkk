# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов. Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
#
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
#
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)
# (это тоже методы)
#
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни)
# (и это тоже метод).


class Flowers:
    def __init__(self, name, freshness_in_days, color, stem_length, cost):
        self.name = name
        self.freshness_in_days = freshness_in_days
        self.color = color
        self.stem_length = stem_length
        self.cost = cost

    def __repr__(self):
        return f'{self.name}'


class Roses(Flowers):
    def __init__(self, name, freshness_in_days, color, stem_length, cost):
        super().__init__(name, freshness_in_days, color, stem_length, cost)


class Tulips(Flowers):
    def __init__(self, name, freshness_in_days, color, stem_length, cost):
        super().__init__(name, freshness_in_days, color, stem_length, cost)


class Orchids(Flowers):
    def __init__(self, name, freshness_in_days, color, stem_length, cost):
        super().__init__(name, freshness_in_days, color, stem_length, cost)


class Peonies(Flowers):
    def __init__(self, name, freshness_in_days, color, stem_length, cost):
        super().__init__(name, freshness_in_days, color, stem_length, cost)


class Bouquet:
    def __init__(self):
        self.bouquet = []

    def add_flower(self, flower):
        self.bouquet.append(flower)

    def total_sum_of_cost(self):
        total_sum = sum(flower.cost for flower in self.bouquet)
        return total_sum

    def average_life_time(self):
        average_life_time = sum(flower.freshness_in_days for flower in self.bouquet) / len(self.bouquet)
        return average_life_time

    def sort_by_parameter(self, parameter):
        if parameter == 'cost':
            self.bouquet.sort(key=lambda x: x.cost)
            print(bouquet.bouquet)
        elif parameter == 'name':
            self.bouquet.sort(key=lambda x: x.name)
            print(bouquet.bouquet)
        elif parameter == 'freshness_in_days':
            self.bouquet.sort(key=lambda x: x.freshness_in_days)
            print(bouquet.bouquet)
        elif parameter == 'color':
            self.bouquet.sort(key=lambda x: x.color)
            print(bouquet.bouquet)
        elif parameter == 'stem_length':
            self.bouquet.sort(key=lambda x: x.stem_length)
            print(bouquet.bouquet)
        else:
            print('Вы ввели неверный параметр')


def search_flower_by_life_time(self, min_day, max_day):
    result_flowers = []
    for flower in self.bouquet:
        if min_day <= flower.freshness_in_days <= max_day:
            result_flowers.append(flower)
    print(result_flowers)


rose = Roses('Роза', 8, 'red', 15, 300)
tulip = Tulips('Тюльпан', 5, 'yellow', 10, 400)
orchid = Orchids('Орхидея', 4, 'pink', 12, 100)
pion = Peonies('Пион', 6, 'blue', 13, 200)

bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(orchid)
bouquet.add_flower(pion)

print(bouquet.total_sum_of_cost())
print(bouquet.average_life_time())
bouquet.sort_by_parameter('cost')
bouquet.search_flower_by_life_time(5, 9)
