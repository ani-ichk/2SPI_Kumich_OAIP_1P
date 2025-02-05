from tuple_sort import tuple_sort
from star import star
from nearby import nearby


def main():
    tuple_sort([('cat', 1, 'ert'), ('bu', 3, 'abc'), ('a', 2, 'de' )])
    star('Выполнить лабораторную, оформить отчёт в файле word.')
    print(*nearby(['100100011', '0001100001',
                   '100001001', '1110010111'], places=4), sep='\n')
    print(*nearby(['111', '101101', '11000']), sep='\n')

if __name__ == '__main__':
    main()