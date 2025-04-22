import gzip
from time import monotonic

# Types of compression:
# one shot: gzip, bzip2 ...
# archives: zip, tar, ...

# wall clock: human time, can jump
# monotonic clock: only goes up, doesn't jump
start = monotonic()
# Get
num_errors = 0
count = 0
with gzip.open('data/http.log.gz', 'rt') as fp:
    for line in fp:
        count += 1
        # Parse
        # in24.inetnebr.com - - [01/Aug/1995:00:00:01 -0400] "GET /shuttle/missions/sts-68/news/sts-68-mcc-05.txt HTTP/1.0" 200 1839
        fields = line.split()
        code = int(fields[-2])

        # Analyze
        if code >= 400:
            num_errors += 1

# Output
duration = monotonic() - start
print(f'processed {count:,} lines in {duration:.2f}sec ({num_errors:,})')