#Given a string input Count all lower case, upper case, digits, and special symbols
input_str = "P@#yn26at^&i5ve"
lower=0
upper=0
digit=0
special=0
for i in input_str:
    if i.islower():
        lower +=1
    if i.isupper():
        upper +=1
    if i.isnumeric():
        digit +=1
    else:
        special +=1

print("There are " +str(digit) + " digits and " + str(lower) + " lower case and "+ str(upper) + " upper case and "+ str(special) + " special letterls")