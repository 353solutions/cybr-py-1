# Handling Dependencies

Limitation: Python can install only one version of a package.
Solution: Use a virtual environment per project.

## Simple Workflow

- `$ python -m venv .venv`
    - Or from your IDE
    - Once per project
- Make sure your IDE and shell uses the same Python from the virtual environment
    - `$ source ./.venv/bin/activate`
- Write down dependencies in a file (requirements.txt)
    - Add it to git
- `$ ./.venv/bin/python -m pip install -r requirements.txt`
    - Every time you add/change a dependency

### Development Dependencies

Sometime you need packages just for development, not for production (e.g. testing)

- Create `dev_requirements.txt`
- Add packages to it
- `$ ./.venv/bin/python -m pip install -r dev_requirements.txt`
    - Only locally/in CI

## Risks of Using 3-party Packages

- Owner deleting the package
- Security (supply chain)
    - Ignorance/lack of resource
    - Malicious
- Bugs
- Breaking API
- Legal
- Package size on disk

## Other Package Managers
- [uv](https://astral.sh/blog/uv) - pip + venv in one, fast, trending
- [poetry](https://python-poetry.org/) - pip + venv in one, fast
- [conda](https://anaconda.org/anaconda/conda) - For scientific computing, does not PyPI
    - Avoid unless you have a good reason