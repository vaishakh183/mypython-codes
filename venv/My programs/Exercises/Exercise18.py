#. Write a Python script to check if a given key already exists in a dictionary.

d1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key=input("Enter a key")

for i in d1:
    if int(key) == i:
        print("Key " + str(key)+ " is available")
