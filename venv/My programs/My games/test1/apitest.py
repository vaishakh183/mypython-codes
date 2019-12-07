import requests
import json
import pprint
import time
#a=requests.get("https://formulae.brew.sh/api/formula.json")
#print(a.status_code)
#pprint.pprint(a.json())
#jsondata=a.json()
#print(type(jsondata))
#pprint.pprint(jsondata[0]['bottle']['stable']['files'])
#package_name=jsondata[0]['name']
#pprint.pprint(jsondata[0]['name'])

#package_url= f'https://formulae.brew.sh/api/formula/{package_name}.json'
#print(package_url)

#statuscode=requests.get(package_url)
#pprint.pprint(statuscode.json())
#content=statuscode.json()
#print(type(content))
#print(content['analytics']['install']['30d'])
#print(content['analytics']['install']['90d'])
#print(content['analytics']['install']['365d'])
#https://formulae.brew.sh/api/formula/a2ps.json
#b=requests.get("https://formulae.brew.sh/api/formula/a2ps.json")
#print(b.status_code)

#find number of installs

#pprint.pprint(statuscode['0'])

#print only names of packages..

a=requests.get("https://formulae.brew.sh/api/formula.json")
jsondata=a.json()
packages=[]
pack=[]
d1=dict()
t1=time.perf_counter()
for count,data in enumerate(jsondata):
    pack_name = data['name']
    package_url = f'https://formulae.brew.sh/api/formula/{pack_name}.json'
    pack_details=requests.get(package_url)
    pack_details_json=pack_details.json()
    content_30d = pack_details_json['analytics']['install']['30d']
    content_90d = pack_details_json['analytics']['install']['90d']
    content_365d = pack_details_json['analytics']['install']['365d']i
#    print(pack_name)
#    d1['name']=pack_name
    d1= {
        'name': pack_name,
        'analysis': {
            '30d':content_30d,
            '90d':content_90d,
            '365d':content_365d
        }
    }
    packages.append(d1)
    if count > 5:
        break
print(packages)
t2=time.perf_counter()
differ=t2-t1
print("Completed in " + str(differ))
with open('packages.json','w') as f:
    json.dump(packages,f)

