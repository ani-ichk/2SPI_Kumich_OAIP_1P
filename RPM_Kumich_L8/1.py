from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int
    price: int


def sorting(book):
    return sorted(book, key=lambda b: b.year)


book = [Book('Преступление и наказание', 'Ф. М. Достоевский', 1866, 210),
        Book('Война и мир', 'Л. Н. Толстой', 1869, 300),
        Book('Анна Каренина', 'Л. Н. Толстой', 1877, 250),
        Book('Мастер и Маргарита', 'М. А. Булгаков', 1967, 230),
        Book('Тихий Дон', 'М. Шолохов', 1940, 280)]

sorted_book = sorting(book)
for i in sorted_book:
    print(i.title, i.author, i.year, i.price)