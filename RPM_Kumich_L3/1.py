def factorial(n):
    if n < 0:
        return 'не существует'
    # 0! = 1! = 1
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print('Факториал', 5, 'равен', factorial(5))