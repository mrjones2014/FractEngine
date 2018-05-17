# FractEngine

A fractal engine written in Python. **This project uses Python 3**.

## Virtualenv

Virtual environment is managed by `pipenv` package. Install `pipenv` by running `pip install pipenv` or `pip3 install pipenv` (depending on your default `pip` version).

To activate the virtual environment for the project, `cd` into the project directory and run `pipenv shell`.

## Coding Conventions

Since Python doesn't have interfaces (or, more accurately, an `interface` keyword), classes that are intended to be
used like an interface should start with a capital `I`; for example `class IFractal:`. Interfaces are actually not
necessary in Python because Python supports multiple inheritence and ducktyping.