from urllib.request import urlopen
# import requests

url = 'https://api.github.com/users/tebeka'

"""HTTP Response
HTTP/1.1 200 OK <- status line
<--> headers
Content-Type: application/json; charset=utf-8
Content-Length: 535
...

<--> body
{
  "login": "tebeka",
  "id": 87697,
  "node_id": "MDQ6VXNlcjg3Njk3",
...
"""

fp = urlopen('https://api.github.com/users/tebeka')
print('status:', fp.status)
print('size:', fp.headers['content-length'])
print('body:', fp.read())
