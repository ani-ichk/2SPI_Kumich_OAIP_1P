class Inventory:
    def __init__(self, items, weight_limit, slots):
        self.__items = items
        self.__weight_limit = weight_limit
        self.__current_weight = sum(v for k, v in self.__items.items())
        self.__slots = slots

    def __str__(self):
        return f'Inventory (capasity: {self.__slots}: {self.__items}).'

    def __iter__(self):
        for k, v in self.__items.items():
            print(f'({k}, {v})')

    def __len__(self):
        return sum(v for k, v in self.__items.items())

    def __getitem__(self, key):
        if key in self.__items:
            return self.__items[key]
        else:
            return 'Такого предмета нет'

    def __setitem__(self, key, value):
        if self.__current_weight + value <= self.__weight_limit:
            if key in self.__items:
                self.__items[key] += value
                return self.__items
            else:
                self.__items[key] = value
                return self.__items
        else:
            return 'Места нет'

    def __delitem__(self, key):
        del self.__items[key]
        return self.__items

    def __contains__(self, item):
        if item in self.__items:
            return f'{item} in inventory'
        else:
            return f'{item} is not in inventory'

    def __add__(self, other):
        if len(self.__items) < self.__slots:
            for k, v in other.items():
                if k in self.__items:
                    self.__items[k] += v
                else:
                    self.__items[k] = v
            return self.__items
        else:
            return 'Недостаточно места'


a = Inventory({'stone': 5, 'wood': 10}, 40, 5)
print(a)
print(len(a))
print(a['stone'])
a['wood'] = 1
a['dimond'] = 2
print(a)
del a['stone']
print('stone' in a)
print(a + {'stone': 5, 'wood': 1})
