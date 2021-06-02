from functools import reduce
import acronym


def is_even(num): return num % 2 == 0


# print(not is_even(9))
numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
even = filter(lambda num: num % 2 == 0, numbers)
# odd = filter(lambda num: num % 2 != 0, numbers)


# def is_odd(n): return not is_even(n)


odd = filter(lambda n: not is_even(n), numbers)
# odd = filter(is_odd, numbers)

# print(*even)
print(*odd)


# total = reduce(lambda a, run_total: a + run_total, [1, 2, 3, 4, 5])
# print(total)

def join_strings(words_list):
    joined_together = reduce(lambda word, putting_together: word + putting_together, words_list)
    print(joined_together)


l = ['hello', 'world', '!']
join_strings(l)

# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_num = [p for p in numbers if p > 0]
print(*positive_num)

numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
even_num = [e for e in numbers if e%2 == 0]
print(*even_num)

words = ["hello", "my", "name", "is", "Sam"]
word_len = [(w.upper(), len(w)) for w in words]
print(word_len)

acronym.generate_acronym()



