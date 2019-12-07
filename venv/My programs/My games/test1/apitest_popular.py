import json
with open('packages.json','r') as f:
#    print(f.readlines())

    data=json.load(f)
print(data)

