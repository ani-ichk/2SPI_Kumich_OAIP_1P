from typing import Generic, TypeVar, List

T = TypeVar('T')  # индификатор
U = TypeVar('U')  # описание
V = TypeVar('V')  # приоритет

class Task(Generic[T, U, V]):
    def __init__(self, task_id: T, description: U, priority: V):
        self.task_id = task_id
        self.description = description
        self.priority = priority

    def __str__(self):
        return f'id: {self.task_id}, description: {self.description}, priority: {self.priority}'


class TaskManager(Generic[T, U, V]):
    def __init__(self):
        self.tasks: List[Task[T, U, V]] = []

    def add_task(self, task_id: T, description: U, priority: V):
        self.tasks.append(Task(task_id, description, priority))

    def get_highest_priority_task(self) -> Task[T, U, V]:
        if not self.tasks:
            return None
        # bool
        if all(isinstance(task.priority, bool) for task in self.tasks):
            for task in self.tasks:
                if task.priority is True:
                    return task
            return self.tasks[0]
        # int
        highest_prior = self.tasks[0]
        for task in self.tasks:
            if task.priority > highest_prior.priority:
                highest_prior = task
        return highest_prior

    def __str__(self) -> str:
        return '\n'.join(str(task) for task in self.tasks)


tasks1 = TaskManager[int, str, int]()
tasks1.add_task(1, 'первое', 4)
tasks1.add_task(2, 'второе', 3)
tasks1.add_task(3, 'третье', 5)

print(tasks1)
print('Наивысший приоритет:', tasks1.get_highest_priority_task())
