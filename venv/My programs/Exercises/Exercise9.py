#Given an input string, count occurrences of all characters within a string

string="Python is an object-oriented programming language created by Guido"
dictionary=dict()

for i in string:
    count=string.count(i)
#    print(i," ",count)
    dictionary[i] =count

print(dictionary)
