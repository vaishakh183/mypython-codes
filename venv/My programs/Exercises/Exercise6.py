#Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
a=input("Enter string")
b=0
for i in a:
    if i.isnumeric():
        b=b+int(i)
print(b)
