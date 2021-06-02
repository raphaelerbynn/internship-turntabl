# numbers from 7-10
# i = 6
# while i < 10:
#     i = i + 1
#     print(i)

# even numbers from 12-20
# n = 20
# while n > 13:
#     if n % 2 == 0:
#         print(n)
#     n = n - 1


def print_even_btn(start, end):
    while start < end:
        if end % 2 == 0:
            print(end)
        end = end - 1


print_even_btn(12, 20)