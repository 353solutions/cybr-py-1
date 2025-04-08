# Truth

x = 10
if x > 5:
    print('OK')


if x:
    print('x is true')

# What is true?
# In Python, everything is true. Except:
# - False
# - Zero (0, 0.0, )
# - Empty collections ([], '', {}, ...)
# - None

shopping_cart = ['banana', 'milk']
# if len(shopping_cart) > 0:
if shopping_cart:  # More Pythonic
    print('you have items in the cart')


# Equality vs identity
cart1 = ['bread', 'butter']
cart2 = ['bread', 'butter']

"""
cart1 ---> ['bread', 'butter']
cart2 ---> ['bread', 'butter']
"""

# equality
if cart1 == cart2:
    print('carts are equal')

# identity
if cart1 is cart2:
    print('carts are same object')
else:
    print('different objects')


cart2 = cart1
"""
cart1 ---> ['bread', 'butter']
           ^
           |
cart2 -----+
"""
if cart1 is cart2:
    print('carts are same object')
else:
    print('different objects')

cart1.append('cheese')
print(cart1, cart2)
