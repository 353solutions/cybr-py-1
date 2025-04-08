# Sync content of two directories
# Talk about files

# File
# - Path to the file (/etc/passwd)
# - The file on disk

from pathlib import Path

# r'' means "raw" string, \ is just a \
csv_file = r'c:\new_reports\tracking\one.csv'
print(csv_file)

p = Path('/var/run/docker.pid')
print(p)
print(p.name)  # last part (docker.pid)
print(p.parent)  # up to name (/var/run)
print(p.suffix)  # extension (.pid)

logs_dir = Path('/var/log')
log_file = logs_dir / 'app.log'
print(log_file)
print(log_file.exists())

ignore_file = Path('~/.config/git/ignore')
print(ignore_file.exists())

ignore_file = Path('~/.config/git/ignore').expanduser()
print(ignore_file.exists())
