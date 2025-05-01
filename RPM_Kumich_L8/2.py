from dataclasses import dataclass
from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def full_name(self):
        pass

    @abstractmethod
    def get_id(self):
        pass

@dataclass
class Student(Person):
    first_name: str
    last_name: str
    student_id: int

    def full_name(self):
        return self.first_name, self.last_name
    def get_id(self):
        return self.student_id

@dataclass
class Teacher(Person):
    first_name: str
    last_name: str
    employee_id: int
    courses: str

    def full_name(self):
        return self.first_name, self.last_name

    def get_id(self):
        return self.employee_id


def print_name_id(person):
    for i in person:
        print(f'name: {i.full_name()}, id: {i.get_id()}')


students = [Student('Максим', 'Трофимович', 11),
            Student('Анастасия', 'Сидорова', 12),
            Student('Екатерина', 'Железнова', 31),
            Student('Иван', 'Иванов', 13)]
teachers = [Teacher('Анастасия', 'Пифагорова', 101, 'математика'),
            Teacher('Татьяна', 'Пушкина', 102, 'русский'),
            Teacher('Елена', 'Тесла', 103, 'физика')]

print('Студенты:')
print_name_id(students)
print('Учителя:')
print_name_id(teachers)