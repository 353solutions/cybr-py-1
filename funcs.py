# Defining & Calling functions


def sub(a, b):
    return a - b


# positional argument
print(sub(1, 7))

# keyword argument
print(sub(b=7, a=1))

print(sub(1, b=7))

# Error: Positional arguments *must* come before keyword
# print(sub(a=1, 7))

args = (1, 7)
# print(sub(args[0], args[1]))
# * in function call it'll unpack sequence to positional
print(sub(*args))
# print(sub(1, 7))

# function are like any other variable
minus = sub
minus(1, 7)

print()
print(1)
print(1, 2)


# * in function definition, it packs positional to a tuple
def var_args(*args):
    # args is a tuple here
    # print(f'args = {args}')
    print(f'{args=}')


var_args()
var_args(1)
var_args(1, 2)

[1, 2, 3]  # list
(1, 2, 3)  # tuple

kw = {'a': 1, 'b': 7}
# ** in function call unpacks a mapping to keyword
print(sub(**kw))
# print(sub(a=1, b=2))


# ** in function definition packs keyword to a dict
def kwargs(**kw):
    # kw is a dict
    print(f'{kw=}')


kwargs(a=1, b=7)


# I (Miki) use **kw to "pass through" option
def print_report(date, **kw):
    data = query_db(date)
    plot(data['dates'], data['values'], **kw)


# b has a default value that's used if the user
# does not provide it
# WARNING: NEVER USE MUTABLE DEFAULT VALUES
# e.g. def append(a, items=[]):
# mutable: list, dict, set


def add(a, b=1):
    return a + b


print(add(1, 7))
print(add(1))


# type annotation
def mul(a: int | float, b: int | float) -> int | float:
    """Returns a times b.

    >>> mul(3, 7)
    21
    """
    return a * b


print(mul(1.1, 3))

# Miki use type annotation for 2 things:
# - Documentation
# - Help auto completion


def append_none(items: list):
    items.append(None)


# lambda: anonymous function
inc = lambda n: n + 1

print(inc(2))


div_call_count = 0

# Use "global" on when re-binding (change what variable points to)
# No need when only reading or mutating (e.g. append to a list)


def div(a, b):
    global div_call_count

    div_call_count += 1
    # print(div_call_count)  # OK
    return a / b


print(div(1, 2))
print(div_call_count)


#
def add_two_numbers(number_one, number_two):
    total = number_one + number_two
    # BUG: recursion
    # print(add_two_numbers(3, 4))
    print(f'add_two_numbers({number_one}, {number_two})')
    print(total)


add_two_numbers(1, 2)
