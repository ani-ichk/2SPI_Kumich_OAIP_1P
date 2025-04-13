from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n < 0:
        return 'не существует'
    # 0! = 1! = 1
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)