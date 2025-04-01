# We already talked on
# - numbers: int, float
# - text: str, bytes

# list
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
    ... # FIXME: Up to you

diffs([1, 3, 7, 10])
# [2, 4, 3]