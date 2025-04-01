# We already talked on
# - numbers: int, float
# - text: str, bytes

### list
cart = ['apple', 'lemon']
cart.append('milk')
print(cart)

print('len:', len(cart))
# Stack/LIFO
last = cart.pop()
print('last:', last)
print('cart:', cart)
cart.extend(['milk', 'honey'])
# cart += ['milk', 'honey]
print('cart:', cart)
# mutation
print(cart.reverse())  # None
# When a method return None, it usually means
# it changed the object
print('cart:', cart)
# reverse & sort are in-place

s = 'hello'
print(s.upper())
print('s:', s)
# re-binding
s = s.upper()  # because str is immutable

# Exercise: diffs
def diffs(nums):
    vals = []
    for i, v in enumerate(nums[1:]):
        diff = v - nums[i]
        vals.append(diff)
    return vals


diffs([1, 3, 7, 10])
# [2, 4, 3]

### tuple

# Ready Player One
player1 = ('Parzival', 139)
print(player1)

print('len:', len(player1))
print('slice:', player1[1:])
# tuples are immutable
# player1[0] = 'Art3mis'  # will fail

l1 = [1]
print('l1:', l1)
# s1 = (1)  # BUG: This is the number 1
s1 = (1,)
# s1 = 1,  # Also possible
print('s1:', s1)

### dict (hash tables)
# mapping from key -> value

# env -> host, port
hosts = {
    'prod': ('srv1', 80),
    'qa': ('srv1', 8080),
}

hosts = {
    'prod': {
        'host:' 'srv1'
        'port': 80,
    },
    'qa': {
        'host': 'srv1', 
        'port': 8080,
    },
}

print(hosts['qa']['port'])

# hero name -> person name
heros = {
    'Superman': 'Clark',
    'Wonder Woman': 'Diana',
    'Batman': 'Bruce',
}

# keys
for key in heros:
    print(key)

# values
for name in heros.values():
    print(name)

for hero, name in heros.items():
    print(f'{hero} is {name}')

print('len:', len(heros))

heros['Batman'] = 'Wayne'
print(heros)

# heros['Aquaman']  # will fail
print('Aquaman:', heros.get('Aquaman'))
print('Superman:', heros.get('Superman'))

if heros.get('Aquaman') is None:
    print('no water')

# if heros.get('Aquaman') == None:
#     print('no water')

if not heros.get('Aquaman'):
    print('no water')

if 'Aquaman' not in heros:
    print('no water')


# TODO:
# What is True
# == vs is