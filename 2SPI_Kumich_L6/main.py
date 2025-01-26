from quarters import quarters
from future import future
from circuit_resistance import circuit_resistance


def main():
    data = [(-5, 1), (-1, 3), (2, -1), (0, 3)]
    for k, v in sorted(quarters(*data).items()):
        print(f'{k}:\t{v}')


if __name__ == '__main__':
    main()