# Run from IDE or in the terminal
#   python -m pytest -v
# Test discovery:
# - Files matching `*_test.py` or `test_*.py`
# - In these files, any function that starts with `test_`

import nlp
import pytest

def test_smoke():
    ...


def test_tokenize():
    text = "Who's on first?"
    expected = ['who', 's', 'on', 'first']
    tokens = nlp.tokenize(text)
    assert expected == tokens


tokenize_cases = [
    ("Who's on first?", ['who', 's', 'on', 'first']),
    ("What's on second?", ['what', 's', 'on', 'second']),
    ("", []),
]

# Exercise: Read the test cases from data/tokenize_cases.yml
# Install PyYAML
# import yaml
# with open('data/tokenize_cases.yml') as fp:
#     data = yaml.safe_load(fp)

# Parameter names must match names in parametrize
@pytest.mark.parametrize('text, expected', tokenize_cases)
def test_tokenize_params(text, expected):
    tokens = nlp.tokenize(text)
    assert expected == tokens


# Aside: Floating points
def test_mul():
    v = 1.1 * 1.1
    assert round(v, 5) == round(1.21, 5)