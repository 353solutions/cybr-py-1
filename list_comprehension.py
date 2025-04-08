from pprint import pprint


# euler 6: https://projecteuler.net/problem=6
def sum_of_squares(n):
    total = 0
    for i in range(n + 1):
        total += i * i
    return total


print(sum_of_squares(10))


def sum_of_squares2(n):
    squares = []
    for i in range(n + 1):
        squares.append(i * i)
    print(squares)
    return sum(squares)


print(sum_of_squares2(10))


def sum_of_squares3(n):
    # List comprehension
    squares = [i * i for i in range(n + 1)]
    return sum(squares)


print(sum_of_squares3(10))

# List comprehension: Generate list from another collection
loons = ['Bugs', 'Daffy', 'Taz']
# change (map)
print([name.lower() for name in loons])
# map + filter
print([name.lower() for name in loons if len(name) > 3])
# SQL: SELECT name.lower() FROM loons WHERE len(name) > 3
# only filter
print([name for name in loons if len(name) > 3])

# symbol,volume,price
# CSV: Comma separated values
trades_text = """\
CSCO,100,18.04
TSLA,200,45.03
CSCO,150,19.05
MSFT,250,80.56
IBM,500,22.01
TSLA,250,44.23
GOOG,200,501.45
CSCO,175,19.56
MSFT,75,80.81
GOOG,300,502.65
IBM,150,25.01
"""

# Convert data to list of dict
# [{'symbol': 'CSCO', 'volume': 100, 'price': 18.04}, ....]

# Split trades_text to lines
lines = trades_text.splitlines()
# Convert line to a dict

line = 'GOOG,300,502.65'


def parse_line(line):
    fields = line.split(',')
    # print(fields)
    # unpacking
    symbol, volume, price = fields
    trade = {
        'symbol': symbol,
        'volume': int(volume),
        'price': float(price),
    }
    return trade


print(parse_line(line))

trades = [parse_line(line) for line in trades_text.splitlines()]
pprint(trades)

# Print unique list of symbols, sorted
# Every time you hear "unique", think set
symbols = set([trade['symbol'] for trade in trades])
print('We are invested in:')
for symbol in sorted(symbols):
    print(f'- {symbol}')

# How many stocks of CSCO do we own?
num_csco = 0  # FIXME
print(f'We own {num_csco} stocks of CSCO')
