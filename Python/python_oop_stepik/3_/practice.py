"""


"""


class Building:
    def __init__(self, quantity):
        self.levels = dict.fromkeys(range(1, quantity + 1), None)

    def __getitem__(self, item):
        if item in self.levels:
            return self.levels[item]

    def __setitem__(self, key, value):
        if key in self.levels:
            self.levels[key] = value

    def __delitem__(self, key):
        if key in self.levels:
            self.levels[key] = None

if __name__ == '__main__':
    iron_building = Building(22)  # Создаем здание с 22 этажами
    iron_building[0] = 'Reception'
    iron_building[1] = 'Oscorp Industries'
    iron_building[2] = 'Stark Industries'
    print(iron_building[2])
    del iron_building[2]
    print(iron_building[2])