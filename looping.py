loons = ['bugs', 'daffy', 'tweety']
colors = ['gray', 'black', 'yellow']

# Print names
for name in loons:
    print(name)

# Print names in reverse order
for name in loons[::-1]:
    print(name)

for name in reversed(loons):
    print(name)

# Print name and its location
for i, name in enumerate(loons):
    print(f'{name} at {i}')

# for e in enumerate(loons):
#     i, name = e
#     print(f'{name} at {i}')

# Print loon and its color
for i, name in enumerate(loons):
    color = colors[i]
    print(f'{name} is {color}')

for name, color in zip(loons, colors):
    print(f'{name} is {color}')

# zip stops after the shortest list is done
for name, color in zip(loons, colors + ['white']):
    print(f'{name} is {color}')

# The below will fail
# for name, color in zip(loons, colors + ['white'], strict=True):
#     print(f'{name} is {color}')

for i, (name, color) in enumerate(zip(loons, colors )):
    print(f'[{i}]: {name} is {color}')

i, (name, color) = [0, ['bugs', 'gray']]