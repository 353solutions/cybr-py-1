"""A 2D game where players collect keys"""

# Think "ford focus" vs a specific car which is of that model
# list is the class and cart is an instance
cart = list()  # cart = []
cart.append('carrots')  # method call

# str is the class, 'hello' is an instance
name = 'hello'  # instance of str
name.upper() # method call

# Classes define behaviour (methods, ...)
# Instances are "dumb", they know only
# - class (__class__)
# - attributes (__dict__, dunder dict)

class Player:
    game = 'OASIS'  # class attribute, shared among instances
    num_players = 0

    # __init__ is a method
    # "self" is provided by Python, it's the current instance
    # ("this" in other languages C++, Java, JavasSript, ...)
    def __init__(self, name):
        self.name = name  # Instance attribute, specific to "self"
        self.x, self.y = 0, 0
        # BUG: Adds num_players to instance
        # it'll shadow num_players from the class
        # self.num_players += 1 
        # Bug fix:
        Player.num_players += 1

    # move is a method, called from instance
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# before __init__
# p1.name = 'Parzival'

# p1 is an instance of Player
p1 = Player('Parzival')
# p1 = Player()
# p1.__init__('Parzival')
print('p1:', p1.name)

p2 = Player('Art3mis')
print('p2:', p2.name)

print('game:', p1.game, p2.game)
print('Player.game:', Player.game)
# Player.name will err
print('num players:', Player.num_players)

# p1.move is a "bound method"
# Player.move is "unbound method" (missing self)
p1.move(50, 70) # Translated to: Player.move(p1, 50, 70)
print('p1 loc:', p1.x, p1.y)

# Exercise:
# Add a "keys" attribute to Player which starts as empty set
# - set()
# - Add a found(key) method that will add key to keys
#    - It should raise ValueError if key is not one of
#      "copper", "jade", "crystal"
#    - A key should be added only once
p1.found('copper')
p1.found('copper')
try:
    p1.found('gold')
    print('this should have failed!')
except ValueError:
    pass  # OK
print(p1.keys)  # [copper]


def find_attribute(obj, attr):
    """Mimic the built-in getattr function"""
    if attr in obj.__dict__:
        print(f'found {attr} in instance')
        return obj.__dict__[attr]

    cls = obj.__class__
    if attr in cls.__dict__:
        print(f'found {attr} in class')
        return cls.__dict__[attr]

    raise AttributeError(attr)

find_attribute(p1, 'name')
find_attribute(p1, 'num_players')
