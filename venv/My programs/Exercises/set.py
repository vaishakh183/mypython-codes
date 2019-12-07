#set dont care about order of its values inside and it remove duplicates.
#execute this multiple times you can see order of values are changing.
#set checks a value present in it more efficient than tuple and list.

set1={"vaishak","madapeedika","test","test"}
print(set1)
print("test" in set1)

#check what are the common cources in two sets.
cs_cources={"Maths","Science","Physics"}
art_cources={"Maths","Art"}
print(cs_cources.intersection(art_cources))
#check what are cources uniquly available in ce cource set.
print(cs_cources.difference(art_cources))

#combine both cources

print(cs_cources.union(art_cources))

#create a emplty set

set1=set()

print(type(set1))
