# Get
poem = """
The Road goes ever on and on
Down from the door where it began
Now far ahead the Road has gone
And I must follow if I can
Pursuing it with eager feet
Until it joins some larger way
Where many paths and errands meet
And whither then I cannot say
"""


counts = {}  # word -> count
# Parse
# split text to words
words = poem.split()
# Analyze
for word in words:
    word = word.lower()
    # counts[word] += 1  # BUG: counts[word] = counts[word] + 1
    counts[word] = counts.get(word, 0) + 1

max_word, max_count = '', 0
for word, count in counts.items():
    if count > max_count:
        max_word, max_count = word, count

# Output
print(max_word)
