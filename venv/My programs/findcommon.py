list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

ll=[a for a in list_a for b in list_b if a==b]
print(ll)
