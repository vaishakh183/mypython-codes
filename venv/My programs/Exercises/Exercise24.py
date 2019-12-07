#Take two lists, say for example these two:
#	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#write a program that returns a list that contains only the elements that are common between thelists(without duplicates).
#Make sure your program works on two lists of different sizes.
import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(len(a))

print(set(a))
result=[i for i in set(a) if i in b]
print(result)