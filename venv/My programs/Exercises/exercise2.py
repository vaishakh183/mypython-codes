#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
string="vaishakh"
#print(string[0])
for i in range(len(string)):
    print(string[i:] + string[:i])