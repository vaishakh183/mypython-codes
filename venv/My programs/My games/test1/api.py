import requests
import json
import pprint
a=requests.get("https://api.dailysmarty.com/posts")
print(a.status_code)
#print(a.json())
#pprint.pprint(a.json()['posts'][0])

#pprint.pprint(a.json()['posts'][0]['url_for_post'])


b=requests.get("https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=0f9e7af331759ded47f09b247f76d85b")
print(b.status_code)
pprint.pprint(b.json())
