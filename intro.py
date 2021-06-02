import math
import numbers
import string

print ("hello")
print ('hello')
# print (hello)

print(4 + 5)
print(8 * 3)
print(4 / 3)
print(4.0 / 3)
print(3 + 5 * 9)

print("abc" + "def")
print("hello" + " " + "world")
print("123" + "5")

first = "hello"
second = "world"
first + " " + second
print(type(first))
print (first)

# name = input("What is your name?")
# type(name)
# age = input("What is your age?")
# type(age)
#
#
# print("________________________________")
# print("________________________________")
#
# # Converts 32 degrees to radian (HINT: math.pi!).
# # Asks the user for a radius then prints out the surface area and volume of a sphere.
# # Tells the user what time of day it is, in a nice format.
# # Splits a sentence into its words
# # Joins a list of words into a sentence. Find TWO ways to do this!
#
#
# degree = 32
# radian = (math.pi/180) * degree
# print("32 degrees to radian: " + str(radian))
#
# print("________________________________")
#
sentence = "I am going to school"
split = ['I', 'am', 'going', 'to', 'school']
split2 = ['and', 'I', 'am']

# split_list = sentence.split(" ")
# print(split_list)


print (' '.join(split + split2))
print (" ".join(split) + " " + " ".join(split2))

# print(str(5) + " : " + str(40));

name = 'ama'
for i in string.digits:
    if name.__contains__(i):
        print(True)
        break




