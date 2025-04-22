import re

# "Who's on first?" -> ['Who', 's', 'on', 'first']
_word_re = re.compile(r'[a-zA-Z]+')


def tokenize(text):
    """Return tokens in text (lower case)."""
    tokens = []
    for word in _word_re.findall(text):
        tok = word.lower()
        tokens.append(tok)

    return tokens
