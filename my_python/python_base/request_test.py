# -*- coding: utf-8 -*-
import requests
import json

url = 'https://api.github.com/events'
r = requests.get(url)
print(r.text)
print(r.text is None)
print(r.status_code)
print(r.content)
print(json.loads(r.text)[0]['actor'])