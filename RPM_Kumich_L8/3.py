from dataclasses import dataclass
from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def get_total_price(self):
        pass

@dataclass
class Item(Product):
    name: str
    price: float
    quantity: int

    def get_total_price(self):
        return self.price * self.quantity


class Order:
    def __init__(self):
        self.default_factory = []

    def __add__(self, other):
        if isinstance(other, Product):
            self.default_factory.append(other)
        else:
            return 'Это не продукт'
        return self.default_factory

    def total_sum(self):
        return sum(i.get_total_price() for i in self.default_factory)

    def sorted_order(self):
        return sorted(self.default_factory, key=lambda product: product.get_total_price())


i1 = Item(name='i1', price=10, quantity=3)
i2 = Item(name='i2', price=15, quantity=4)
i3 = Item(name='i3', price=5, quantity=4)
i4 = Item(name='i4', price=15, quantity=2)
i5 = Item(name='i5', price=20, quantity=1)
order = Order()
order + i1
order + i2
order + i3
print(order.total_sum())
order + i4
order + i5
print(order.total_sum())
order + i3
print(order.total_sum())
for i in order.sorted_order():
    print(i)