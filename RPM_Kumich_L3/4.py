import time
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() # начало измерения времени
        try:
            res = func(*args, **kwargs)  # вызов функции
            logging.info(f'Функция: {func.__name__}, аргументы: {args}, {kwargs}, '
                         f'результат: {res}, время выполнения: {time.time() - start_time:.10f} секунд')
            return res
        except Exception as e: # исключения
            logging.error(f'Ошибка в функции: {func.__name__}, '
                          f'Аргументы: {args}, {kwargs}, Ошибка: {e}')
            raise
    return wrapper

@log
def factorial(n):
    if n < 0:
        return 'не существует'
    # 0! = 1! = 1
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print('Факториал', 5, 'равен', factorial(5))