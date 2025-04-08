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

TBD


<!--
### Exercises

#### Stocks

Write a function `related_stocks(symbol)` that will return a dict with stocks mentioned when calling stocktweets API.

For example, to get information about `AAPL`, use the following URL: `https://api.stocktwits.com/api/2/streams/symbol/AAPL.json`.
If you look at [the output](data/aapl.json) you can that for every message in the `messages` section there's a `symbols` section.

#### Count Errors

How many requests in [http.log.gz](data/http.log.gz) resulted in an error (status code >= 400)?
-->


### Links

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
