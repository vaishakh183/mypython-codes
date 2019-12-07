#Write a Python program to combine two dictionary adding values for common keys. Go to the editor
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3= dict()
for i,j in d1.items():
    for k,l in d2.items():
        if i == k:
            sum=j+l
            d3[i]=sum
        else:
            d3[i]=j

print(d3)