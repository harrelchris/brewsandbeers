# Brews and Beers

Review and recommendation application for breweries and beers.

## Setup

### Prepare your environment

Run the `setup` script

```shell
scripts\setup
```

## Testing

Run pytest with coverage and generate reports for both

```shell
coverage erase && coverage run -m pytest --html=.reports/pytest/index.html --self-contained-html && coverage html
```

Use the `test` script to run Pytest and Coverage and generate reports for both, or run them individually as needed. Tox is also included to run your tests on multiple Python versions if you have them installed.

#### Windows

```shell
scripts\test
```

### Pytest

A test framework that makes it easy to write small, readable tests.

[Documentation](https://docs.pytest.org/)

```shell
python -m pytest --html=.reports/pytest/index.html --self-contained-html
```

### Coverage

A tool that measures how much of your code is executed during your tests. Aim for 100%.

[Documentation](https://coverage.readthedocs.io/)

```shell
coverage erase && coverage run -m pytest && coverage html
```

### Tox

Test runner that will run your test suite using multiple versions of Python if they are found on your machine.

[Documentation](https://tox.wiki/en/latest/)

```shell
tox
```

## Code Quality

Code quality is enforced using the pre-commit framework with a number of hooks.

### Pre-Commit

Run multiple code quality tools on git-staged code.

[Documentation](https://pre-commit.com/)

```shell
pre-commit run --all-files
```
