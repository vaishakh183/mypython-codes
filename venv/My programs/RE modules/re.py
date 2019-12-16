import re
print("\t Hi")
print(r"\t Hi")

text_to_search="hi vaihsakh vk madapeediaka bangalore india hi hi"
pattern=re.compile(r"hi")
match=pattern.finditer(text_to_search)
for word in match:
    print(word)