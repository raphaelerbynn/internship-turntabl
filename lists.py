def print_btn(min, max):
    l = []
    while min < max-1:
        min = min + 1
        if min % 2 == 0:
            l.append(min)
    return l


print(print_btn(4, 10))
