def cache(func):
    cache_res = {}

    def wrapper(n):
        if n in cache_res:
            return cache_res[n]
        else:
            res = func(n)
            cache_res[n] = res
            return res
    return wrapper

@cache
def factorial(n):
    if n < 0:
        return 'не существует'
    # 0! = 1! = 1
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)