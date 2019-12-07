#arrange String characters such that lowercase letters should come first.
#string="asbAQWEWEsdfsdWQWQ"
#lower=[]
#upper=[]
#letter =""
#for i in string:
#    if i.islower():
#        lower.append(i)
#    else:
#        upper.append(i)
#word = lower+upper
#for j in word:
#    letter = letter+j

#print(letter)

#############################

string="qweqwREERFRGWWERads"
lower=[]
upper=[]
letter =""
for i in string:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
print(letter.join(lower+upper))


