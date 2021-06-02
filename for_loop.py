def any_func():
    for i in range(1, 5):
        print("*" * i)

    for j in range(3, 0, -1):
        print("*" * j)


def contains_a(string):
    if "a" in string:
    # if string.__contains__("a"):
        return True
    return False



def contains_s(s):
    for i in s:
        if i == "s":
            return True
    return False


def contains_m_s(string):
    for i in string:
        if i == "m" and contains_s(string):
            return True
    return False


def evens(list_num):
    total_even = 0
    for i in list_num:
        if i%2 == 0:
            total_even = total_even + i
    return total_even


l = [1, 3, 5, 6, 2, 4]


def check_s(sentence):
    i = -1
    while i < len(sentence):
        i = i+1
        if sentence[i] == "s":
            return True
        return False


# def check_m_s(s):
#     i = -1
#     while i < len(s):
#         i = i+1
#         if s[i] == "m":
#
#         return False


# print(check_m_s("asm"))


# print(contains_a("kofa"))
# print(contains_m_s("mumumiw"))
# print(evens(l))
# print(contains_m_s(""))


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Your year", year, "is a leap year")
        return True
    print("Your year", year, "is a not leap year")
    return True


is_leap_year(2000)
is_leap_year(2100)
is_leap_year(2200)
is_leap_year(2016)




