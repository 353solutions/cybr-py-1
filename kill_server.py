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


def kill_server(pid_file):
    fp = open(pid_file)
    data = fp.read()
    pid = int(data)
    # simulate kill
    print(f'killing server with pid {pid}')


kill_server('server.pid')
