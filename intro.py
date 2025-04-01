# REPL: Read, Eval, Print Loop
# When your run "python intro.py"
# It does only RE (no print or loop)

3 * 7
# SHIFT+ENTER to run selection

7 / 3

# Two types of numbers
# - int: whole number
# - float: decimal numbers (no accurate)
0.1 + 0.2

2**10  # ** is the power operator
2**1000  # Python numbers can grow as much as needed

import math
# See also statistics module

# In scripts/code you need to explicitly print
print(math.sqrt(2))

# Notebook are great for EDA
# Exploratory Data Analysis

# kb is a variable
# variables don't have a type
# the object they point to does
kb = 2**10
10 * kb

kb = 'kilobyte'
print(kb)

type(kb)  # str

count = 10
if count > 5:
    print('big enough')
print('out of if')

# Use 4 spaces for indentation
# Except when in Google :)

if count > 50:
    print('big enough')
elif count > 10:
    print('biggish')
else:
    print('small')

if (count > 5 and count < 20) or count < 0:
    print('just right')

# Most of the time we spend reading code
# Code for readability

# Always code as if the guy who ends up maintaining your code
# will be a violent  psychopath who knows where you live.
#    - Martin Golding

# range starts at 0
# range is half-open, upto but not including
for i in range(4):
    print(i)

for i in range(1, 6):
    print(i)

7 % 2  # modulo/reminder

s = 0
s += 7  # s = s + 7
s += 3
print(s)

# Exercise: Euler 1
# https://projecteuler.net/problem=1
# Solution: 233168

# print(233168)
# GPAO: Get, Parse, Analyze, Output

total = 0
# Get
for n in range(1000):
    # Parse: NOP
    # Analyze
    if n % 3 == 0 or n % 5 == 0:
        total += n
# Output
print(total)
