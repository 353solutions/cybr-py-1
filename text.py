# Working with strings

# 4 ways of creating strings
# All of the below 4 are the same string
s = 'hi'
s = "hi"
s = '''hi'''
s = """hi"""

# Use triple for multi-line strings
poem = '''
The Road goes ever on and on
Down from the door where it began.
Now far ahead the Road has gone,
And I must follow, if I can,
Pursuing it with eager feet,
Until it joins some larger way
Where many paths and errands meet.
And whither then? I cannot say.
'''
# Bilbo Baggins, LOTR

book = 'The Colour of Magic'
print('first:', book[0])
# str is immutable
# book[0] = 't'  # Will raise an exception
print(len(book))
print('last:', book[-1])
print(book[:4])  # slicing operator (half-open)
print(book[4:])
print(book[4:10:2]) # start, stop, step
print(book[::-1])  # Reverse string
print(book[1:10:-1])  # empty string
print(book[:101])  # won't fail
# print(book[100])  # will fail, bounds checking
print('upper:', book.upper())
# upper is a "bound method"
print('the' == 'The')
print('the'.upper() == 'The'.upper())
# Use casefold for case insensitive comparison
print('the'.casefold() == 'The'.casefold())
print('o:', book.count('o'))
print('us book:', book.replace('Colour', 'Color'))

city = ' las vegas strip '
print('city:', city.strip())  # strip whitespace from left & right

city = ' New York      '
print('city:', city.strip())  # strip whitespace from left & right

city = '_New_York__'  # strip _
print(city.strip('_'))

for c in 'hello':
    print(c)


def add(a, b):
    """Return a + b"""
    return a + b

add(7, 4)

int('3')  # str -> int

def sum_of_digits(s):
    """
    >>> sum_of_digits('123')
    6
    >>> sum_of_digits('')
    0
    """
    # FIXME: Your code goes here
    total = 0
    # Get
    for c in s:
        # Parse
        n = int(c)
        # Analyze
        total += n
    return total

print(sum_of_digits('123'))
print(sum_of_digits(''))

def sum_of_digits2(s):
    if len(s) == 0:
        return 0

    total = 0
    n = int(s)
    while n > 0:
        total += n % 10
        n = n // 10 # total //= 10
    return total
    
print(sum_of_digits2('123'))
print(sum_of_digits2(''))

nums = '12\n34\n'
print(nums)
# no_nl = nums.replace('\n', '')
# print(no_nl)
nums = nums.replace('\n', '')
print(nums)

greet = 'שלום'
print(greet[0])

data = greet.encode()
print('len(data):', len(data))
print(data.decode())

# Getting data: bytes -> str (decode)
# Emitting data: str -> bytes (encode)
# Internally work with str

# Windows files, regular expressions

# csv_file = 'c:\taxes\new\2025.csv'  # BUG: \t is tab
# r'' is a "raw" string, \ is just a \
csv_file = r'c:\taxes\new\2025.csv'
print(csv_file)

what, price = 'banana', 12.3
# f'' is f-string (formatted)
s = f'{what} costs {price}, {price}!'
print(s)

name = 'Claude'
print(f'|{name:>20}|')
print(len(f'{name:>20}'))

import math

# only two digits after the decimal
print(f'pi = {math.pi:.2f}')

price = 17
# at least 4 digits, pad with zero
print(f'price = {price:04d}')

print('x' * 10)


def banner(s, width):
    ...  # FIXME: Your code goes here
    print(f'{s:^{width}}')
    print('-' * width)


def banner2(s, width):
    padding = (width - len(s))//2
    print(' ' * padding, end='')
    print(s)
    print('-' * width)


banner("Hi", 6)
#   Hi
# ------