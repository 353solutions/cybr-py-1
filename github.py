from urllib.request import urlopen, HTTPError

import json
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

"""JSON
Serialization: Convert a type in Python to a sequence of bytes (and back)
We do it since computers can send/store only bytes

# JSON <- Type -> Python
null <-> None
true/false <-> True/False
number <-> int/float
string <-> string
array <-> list
object <-> dict

MIA:
string/number <-> datetime
string (base64) <-> bytes

# json API
loads/dumps: bytes/str
load/dump: file like objects
"""

with urlopen('https://api.github.com/users/tebeka') as fp:
  print('status:', fp.status)
  print('size:', fp.headers['content-length'])
  # print('body:', fp.read())
  reply = json.load(fp)

print('name:', reply['name'])
print('num_repos:', reply['public_repos'])

# Exercise: Write a function user_info(login)
# That will return user name and number of public repos
# If there's an error (urlopen raises URLError)
# return ('', 0)
# >>> user_info('tebeka')
# ('Miki Tebeka', 85)

def user_info(login):
  """Return user name and number of repos from GitHub API.

  >>> user_info('tebeka')
  ('Miki Tebeka', 85)
  """
  # TODO: urlencode login?
  url = 'https://api.github.com/users/' + login
  try:
    with urlopen(url) as fp:
      reply = json.load(fp)
  except HTTPError:
    return ('', 0)

  return (reply['name'], reply['public_repos'])

user_info('tebekaxxx')

