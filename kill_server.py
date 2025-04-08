# Server stores process ID in a file
# read file and kill the server


# read content of PID file
# convert PID from str to an int
# issue a kill command

# open mode:
# - read (r) default, write (w), append (a)
# - text (t) default , binary (b)
# open()  # rt
# open('rb')  - read binary
# open('w') - write text, will delete previous content

# Error handling approaches: LBYL vs EAFP
# LBYL: Look before you leap
# EAFP: Easier to as for forgiveness than permission

# Resource: Something we have limited amount of
# Examples: open files, data connections, ...
# Use "with" to make sure you release a resource
# support "with": files, lock, url requests, ...

from pathlib import Path


def kill_server(pid_file):
    # "with open" makes sure that fp will be closed
    # Rule of thumb: Always open files with "with open"
    with open(pid_file) as fp:
        data = fp.read()

    try:
        pid = int(data)
    except ValueError as err:
        msg = f'{pid_file}: {err}'
        raise ValueError(msg) from err
    # simulate kill
    print(f'killing server with pid {pid}')


pid_file = Path('server.pid')
# if pid_file.exists():  # LBYL
# In Python we prefer EAFP
try:
    # Inside try is the happy path
    kill_server(pid_file)
except (FileNotFoundError, OSError):
    print(f'warning: {pid_file} - no such file')
except ValueError as err:
    print(f'error: corrupted pid file: {err}')
finally:  # Code in finally always run
    pid_file.unlink(missing_ok=True)
# except Exception:
#   print('unknown exception')

print('server is down')


# --- Aside: exceptions are non-local exit


def a():
    print('a start')
    b()
    print('a end')


def b():
    print('b start')
    c()
    print('b end')


def c():
    print('c start')
    raise ValueError('a')
    # return
    print('c end')


a()

# call stack
# - a
# - b
# - c

### Aside: with
with open('kill_server.py') as fp:
    print('in: ', fp.closed)
    # 1/0

print('out:', fp.closed)

### Aside: assert

x = 10
assert x > 5, 'x too small'
assert x > 50, 'x too small'


# What built-in assert does
def Assert(condition, error):
    if condition:
        return

    raise AssertionError(error)


Assert(x > 5, 'x too small')
Assert(x > 50, 'x too small')
