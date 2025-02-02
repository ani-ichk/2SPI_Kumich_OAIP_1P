from factorial import factorial
from fibonacci import fibonacci
from prime_num import prime_num

def main():
    print(factorial(3))
    print(fibonacci(4))
    print('YES' if prime_num(1) else 'NO')


if __name__ == '__main__':
    main()