import json
import requests
r = requests.get('https://jsonplaceholder.typicode.com/users', auth=('user', 'pass'))
# d = json.loads(r.json())
print (r.json()[8]['username'])