Aw, Al, Ah = map(float, input('Введите ширину, длину и высоту большой коробоки через пробел: ').split())
big_val = Aw * Al * Ah
small_val = 0
while True:
    a = list(map(float, input('Ширина, длина и высота маленьких коробок через пробел: ').split()))
