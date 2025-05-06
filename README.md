# Python Workshop @ CyberArk

Miki Tebeka
📬 [miki@353solutions.com](mailto:miki@353solutions.com), 𝕏 [@tebeka](https://twitter.com/tebeka), 👨 [mikitebeka](https://www.linkedin.com/in/mikitebeka/), ✒️[blog](https://www.ardanlabs.com/blog/)

[Syllabus](https://docs.google.com/document/d/1p_GIXY2FXOauoPM2QITLdi5UpoCo6oH-9NdOlXehv6w/edit)

#### Shameless Plugs

- [LinkedIn Learning Classes](https://www.linkedin.com/learning/instructors/miki-tebeka)
- [Books](https://pragprog.com/search/?q=miki+tebeka)

---

## Day 1: Getting Started

### Agenda

- Intro to Python and its ecosystem
- Working with the Python REPL
- Working with text: str/bytes, formatting
- Collections: list, tuple, dict & set
- Slicing & List comprehensions
- Control flow & logic
- Iteration & iteration utilities

### Code

- [intro.py](intro.py) - Introduction to Python, looping, variables ...
- [euler8.py](euler8.py) - Project Euler #8
- [text.py](text.py) - Working with text, `str` and `bytes`
- [looping.py](looping.py) - Looping utilities: `range`, `enumerate`, `zip`, `reversed`
- [data_types.py](data_types.py) - More data types: `list`, `tuple`, `dict`

### Exercises


#### Word Frequency

What is the most common word in `data/road.txt` ignoring case?

#### Stocks

Look at data/stocks.csv

You can read the content using the following code:

```python
with open('data/stocks.csv') as fp:
    data = fp.read()
```

Answer the following questions:
- Print sorted unique list of symbols (CSCO ...)
- Print how many stocks of CSCO we own (symbol)
- Print how much money we've invested (price * volume)

Using the data from `data/prices.csv`, print how much we've gained or lost.

### Links

- [How to Think Like a Computer Scientist: Interactive Edition](https://runestone.academy/ns/books/published/thinkcspy/index.html)
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
    - [text](https://docs.python.org/3/tutorial/introduction.html#text)
    - [lists](https://docs.python.org/3/tutorial/introduction.html#lists)
    - [Errors & exceptions](https://docs.python.org/3/tutorial/errors.html)
- [pythontutor](https://pythontutor.com/) - Visualize Python execution
- [itertools module](https://docs.python.org/3/library/itertools.html#itertools.count)
    - Read and understand the "Itertools Recipes" section
- Iterators
    - [Iterators](https://docs.python.org/3/tutorial/classes.html#iterators) in the Python tutorial
    - [itertools](https://docs.python.org/3/library/itertools.html) - Iterator utilities (good reading ☺)
    - [Generator Tricks for System Programmers](http://www.dabeaz.com/generators/)
    - [Generators: The Final Frontier](https://www.youtube.com/watch?v=D1twn9kLmYg)
- [Python Type Conversion](https://www.mermaidchart.com/raw/493b268f-89ca-4129-b83a-8d8cd64602e0?theme=light&version=v0.1&format=svg)
- [List of Unicode Characters](https://en.wikipedia.org/wiki/List_of_Unicode_characters)
- [Project Euler](https://projecteuler.net/)
- [Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Google Colab](https://colab.research.google.com/) - Notebooks in the cloud


### Data & Other

- [http.log.gz](data/http.log.gz)
- [road.txt](data/road.txt)
- ☺
- ♡

---

# Day 2: Working with Python

### Agenda

- List comprehensions
- Defining & calling functions
- Working with files
- Handling resources using `with`
- Error handling
- Modules & packages (imports)
- Calling REST APIs


### Code

- [equal.py](equal.py) - Identity vs equality
- [funcs.py](funcs.py) - Defining & calling functions
- [github.py](github.py) - Get user info from GitHub, JSON
- [imports.py](imports.py) - Importing modules
- [kill_server.py](kill_server.py) - Error handling
- [list_comprehension.py](list_comprehension.py) - List comprehensions
- [sync.py](sync.py) - Sync context of two directories
- [word_freq.py](word_freq.py) - Word frequency

### Exercises

#### Count Errors

How many requests in [http.log.gz](data/http.log.gz) resulted in an error (status code >= 400)?
Use `gzip.open` to read the file.

Example lines:
```
uplherc.upl.com - - [01/Aug/1995:00:00:08 -0400] "GET /images/ksclogo-medium.gif HTTP/1.0" 304 0
uplherc.upl.com - - [01/Aug/1995:00:00:08 -0400] "GET /images/MOSAIC-logosmall.gif HTTP/1.0" 304 0
uplherc.upl.com - - [01/Aug/1995:00:00:08 -0400] "GET /images/USA-logosmall.gif HTTP/1.0" 304 0
ix-esc-ca2-07.ix.netcom.com - - [01/Aug/1995:00:00:09 -0400] "GET /images/launch-logo.gif HTTP/1.0" 200 1713
uplherc.upl.com - - [01/Aug/1995:00:00:10 -0400] "GET /images/WORLD-logosmall.gif HTTP/1.0" 304 0
slppp6.intermind.net - - [01/Aug/1995:00:00:10 -0400] "GET /history/skylab/skylab.html HTTP/1.0" 200 1687
piweba4y.prodigy.com - - [01/Aug/1995:00:00:10 -0400] "GET /images/launchmedium.gif HTTP/1.0" 200 11853
slppp6.intermind.net - - [01/Aug/1995:00:00:11 -0400] "GET /history/skylab/skylab-small.gif HTTP/1.0" 200 9202
```

### Links

- Programming Exercises:
    - [exercism](https://exercism.org/tracks/python/exercises)
    - [LeetCode](https://leetcode.com/problemset/all/)
    - [Codewars](https://www.codewars.com/kata)
    - [Project Euler](https://projecteuler.net/archives)
- [HTTP in cats](https://http.cat/)
- [The Zen of Python](https://www.python.org/dev/peps/pep-0020/) (or `import this`)
- [Year 2038 problem](https://en.wikipedia.org/wiki/Year_2038_problem)
- [List comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) in the Python tutorial
- [Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) in the Python tutorial
- [pathlib](https://docs.python.org/3/library/pathlib.html) module - Handling file paths
- [shutil](https://docs.python.org/3/library/shutil.html) module - shell like utlities
- [Context Managers and Python's "with" Statement](https://realpython.com/python-with-statement/)
- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) in the Python tutorial
- [Modules](https://docs.python.org/3/tutorial/modules.html) in the Python tutorial
- [JSON](https://www.json.org/json-en.html) specification
- Python's [json](https://docs.python.org/3/library/json.html) module
- [A typical HTTP session](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Session)

### Data & Other

- [http.log.gz](data/http.log.gz)
- `https://api.github.com/users/tebeka`

---

## Day 3

### Agenda

- OO Basics
	- Classes and instances
	- Methods
	- Special methods
	- Inheritance
- Managing dependencies with pip
- Tesing with pytest
	- Test cases
	- Parametrized tests
	- Fixtures

### Code

- [num_http_errors.py](num_http_errors.py) - Count errors in `http.log.gz`
- [github.py](github.py) - Get user info from GitHub, JSON
- [game.py](game.py) - OO
- [class_utils.py](class_utils.py) - Class creation utilities (namedtuple, dataclass)
- [nlp_test.py](nlp_test.py) - Testing with PyTest
    - [nlp.py](nlp.py) - Tested code
    - [Makefile](Makefile) - Test automation

### Exercises

#### Stock Tweets

Write a function `related_stocks(symbol)` that will return a list of stocks mentioned when you query this symbol on stocktweets.com.

To find about `AAPL` use `https://api.stocktwits.com/api/2/streams/symbol/AAPL.json`

#### A Tests Class

Write a `Tests` class that helps a teacher with student grades.

It should have the following methods:
- `add_score(student, test, score)` - add a score for a student
- `student_avg(student)` - return the average score for a student
- `test_avg(test)` - return the average score for a test

Write tests for the class using `pytest`.


### Links

- [Classes](https://docs.python.org/3/tutorial/classes.html) in the Python tutorial
- [Installing packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [Using Python's pip to Manage Your Projects' Dependencies](https://realpython.com/what-is-pip/)
- Other package managers
    - [uv](https://astral.sh/blog/uv)
    - [poetry](https://python-poetry.org/)
    - [pipenv](https://pipenv.pypa.io/en/latest/)
    - [conda](https://docs.conda.io/en/latest/)
- [pytest](https://docs.pytest.org/en/stable/)
- Linters
    - [ruff](https://docs.astral.sh/ruff/)
    - [flake8](https://flake8.pycqa.org/en/latest/)
    - [pylint](https://www.pylint.org/) - need configuration
    - [bandit](https://bandit.readthedocs.io/en/latest/) - security
- [colab notebook](https://colab.research.google.com/drive/1zrdnYbUfH6Pklqd6ur2tT_msbFTvZH0S?usp=sharing)
- [Beyond PEP8](https://www.youtube.com/watch?v=wf-BqAjZb8M)

### Data & Other

- [tokenize_cases.yml](data/tokenize_cases.yml)

---

## Day 4: Data Processing with Pandas

- Pandas overview
- Loading data
- Selecting data
- Running calculations
- Grouping data
- Cleaning data
- Visualization

### Code

TBD

### Links

- [Pandas](https://pandas.pydata.org/)
    - [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
    - [Indexing and selecting data](https://pandas.pydata.org/docs/user_guide/indexing.html)
    - [Group by: split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html)
- Visualization
    - [matplotlib](https://matplotlib.org/)
    - [plotly](https://plotly.com/python/)
- [NYC Taxi](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- [Kaggle](https://www.kaggle.com/) - Data science competitions

### Data & Other

- [March 2020 Yellow Taxi Trip Records](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-03.parquet)
    - [Data Dictionary - Yellow](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-03.parquet)
    - `curl -LO https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-03.parquet`
- [NYC_Weather_2016_2022.csv.gz](data/NYC_Weather_2016_2022.csv.gz)
