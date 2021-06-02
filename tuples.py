def partition(num):
    t = ()
    if num % 2 == 0:
        return t + (num, None)
    return t + (None, num)


print(partition(10))

