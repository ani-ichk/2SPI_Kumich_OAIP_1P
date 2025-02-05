def tuple_sort(t):
    print(sorted(t, key=lambda x: (x[2], x[1], len(str(x[0])), -x[1])))