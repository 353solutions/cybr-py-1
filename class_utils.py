from collections import namedtuple
from dataclasses import dataclass

# class Location:
#     def __init__(self, lat, lng):
#         self.lat = lat
#         self.lng = lng
#
#     def __repr__(self):
#         cls = self.__class__.__name__
#         return f'{cls}({self.lat!r}, {self.lng!r})'

Location = namedtuple('Location', 'lat lng')

loc = Location(23.7, 43.239)
print(loc)
print(loc[0])
print(loc.lat)
print(len(loc))

# @ means a decorator
@dataclass
class Player:
    name: str
    x: int = 0
    y: int = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

p1 = Player('Parzival')
print(f'{p1=}')
p1.move(10, 37)
print(f'{p1=}')

# Use namedtuple for immutable "bag of attributes"
# Use dataclass if you want methods or mutablity
# Use a regular class if you need custom logic in __init__
#   or __post_init__ in dataclass