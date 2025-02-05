def nearby(l, places=1):
    # критерий отбора - n подряд идущих нулей в эл-те списка
    return filter(lambda x: '0' * places in x, l)