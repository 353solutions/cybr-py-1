import json
import math
import sys
import uuid

print('sys:', sys)  # built-in
print('uuid:', uuid)
print('json:', json)
print('math:', math)

"""
Import algorithm:
for every path in sys.path
    look for a module (file.py, dir/__init__.py, file.so ...)
    and load it

Use PYTHONPATH environment variable to prepend to sys.path
"""

# If name is self explaining, use this format
from urllib.request import URLError, urlopen

try:
    # with urllib.request.urlopen('https://example.com'):
    with urlopen('https://example.com'):
        pass
except URLError:
    print('error')

# Is name is ambigous/too general, use this format
import json

# dumps by itself is not self explain, since
# it might come from yaml, json, pickle, ...
data = json.dumps({'lat': 32.7, 'lng': 31.5})

# import numpy as np
# import pandas as pd
import statistics as st

st.median([1, 3, 2, 4])

# NEVER DO: from math import *
e = 7
print(f'{e=}')
from math import *

print(f'{e=}')

"""
import go at top of the file
sort them alphabetically
    - IDE: Organize import
"""
