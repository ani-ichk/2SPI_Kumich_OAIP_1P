from typing import Generic, TypeVar


T = TypeVar('T')


class TypedArray(Generic[T]):
    def __init__(self):
        self.array = []

    def add(self, item: T):
        self.array.append(item)

    def get(self, index):
        if -len(self.array) <= index < len(self.array):
            return self.array[index]
        else:
            return 'Выход за пределы массива'

    def __str__(self):
        return str(self.array)


ar = TypedArray[int]()
ar.add(1)
ar.add(2)
ar.add(3)
print(ar)
ar.add(4)
print(ar.get(-3))
print(ar.get(3))