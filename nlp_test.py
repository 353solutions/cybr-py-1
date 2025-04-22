# Run from IDE or in the terminal
#   python -m pytest -v
# Test discovery:
# - Files matching `*_test.py` or `test_*.py`
# - In these files, any function that starts with `test_`

# Execute a debugger on failure:
#   python -m pytest -v --pdb

import nlp
import pytest
import yaml
import sqlite3

def test_smoke():
    ...


def test_tokenize():
    text = "Who's on first?"
    expected = ['who', 's', 'on', 'first']
    tokens = nlp.tokenize(text)
    assert expected == tokens


# Before exercise
# tokenize_cases = [
#     ("Who's on first?", ['who', 's', 'on', 'first']),
#     ("What's on second?", ['what', 's', 'on', 'second']),
#     ("", []),
# ]

def load_tokenize_cases():
    with open('data/tokenize_cases.yml') as fp:
        data = yaml.safe_load(fp)

    # return [
    #     (case['text'], case['tokens']) for case in data
    # ]
    cases = []
    for case in data:
        params = (case['text'], case['tokens'])
        if 'name' in case:
            params = pytest.param(*params, id=case['name'])
        cases.append(params)
    return cases

# Exercise: Read the test cases from data/tokenize_cases.yml
# Install PyYAML
# import yaml
# with open('data/tokenize_cases.yml') as fp:
#     data = yaml.safe_load(fp)


# Parameter names must match names in parametrize
@pytest.mark.parametrize('text, expected', load_tokenize_cases())
def test_tokenize_params(text, expected):
    tokens = nlp.tokenize(text)
    assert expected == tokens


@pytest.fixture
def db():
    # setup
    conn = sqlite3.connect(':memory:')

    yield conn

    # teardown
    conn.close()


def test_db(db):
    db.execute('SELECT 1')


# Aside: Floating points
def test_mul():
    v = 1.1 * 1.1
    assert round(v, 5) == round(1.21, 5)