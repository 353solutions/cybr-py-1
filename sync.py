# Sync content of two directories
# Talk about files

# File
# - Path to the file (/etc/passwd)
# - The file on disk

from datetime import datetime
from pathlib import Path
from shutil import copy

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

for py_file in Path('.').glob('**/*.csv'):
    print(py_file)

info = py_file.stat()
# st_mtime is in epoch: seconds since Jan 1, 1970 UTC
print('modification time: ', info.st_mtime)
print('modification time: ', datetime.fromtimestamp(info.st_mtime))


def should_copy(src_file: Path, dest_file: Path):
    if not dest_file.exists():
        return True

    src_mtime = src_file.stat().st_mtime
    dest_mtime = dest_file.stat().st_mtime
    return src_mtime > dest_mtime


def sync(src: Path | str, dest: Path | str):
    """Copy all files from src to dest that are missing or newer."""
    src, dest = Path(src), Path(dest)

    assert src.exists() and src.is_dir(), (
        f'{src} is does not exists or is not a directory'
    )

    # parents=True means create intermediate directories
    dest.mkdir(parents=True, exist_ok=True)

    for src_file in src.glob('**/*'):
        if not src_file.is_file():
            continue

        dest_file = dest / src_file.relative_to(src)
        if should_copy(src_file, dest_file):
            print(f'{src_file} -> {dest_file}')
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            copy(src_file, dest_file)


sync('data', '/tmp/backup/data')
