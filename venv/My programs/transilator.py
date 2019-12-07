#convert all vowel letter to "g" ex: cat --> cgt

def transilator(word):
    a=""
    for i in word:
        if i.lower() in "aeiou":
            a=a+"g"
        else:
            a=a+i
    return a

print(transilator("vaishakh"))

