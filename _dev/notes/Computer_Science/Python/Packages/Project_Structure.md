## Single-File Project Structure

At its minimum a Python package can just be one main Python file:

```
/Project/
   package.py
   setup.py
   README
```

## Minimal Project Structure

```
/Project/
    package/
       __init__.py
       main.py
       helpers.py
       ...
    test/
        main_test.py
        helpers_test.py
        ...
    requirements.txt
    setup.py
    LICENSE
    README
```

## Practical Project Structure

Everyone has their own twist on project structure, so here is my very opinonated practical project structure.

```
/Project/
   .venv/
   package/
        __init__.py
        main.py
        helpers.py
        ...
    test/
        main_test.py
        helpers_test.py
        ...
   pyproject.toml
   README
   LICENSE
   Makefile
```

**Changes**

- Make for macros

  ```
  make [command]
  ```

* Replaces `setup.py` and `requirements.txt` with `pyrpoject.toml` in anticipation for [PEP 517](https://www.python.org/dev/peps/pep-0517/) and [PEP 518](https://www.python.org/dev/peps/pep-0518/). 

**Things not covered**

- Documentation
  The choice yours (e.g., GitHub wiki, readthedocs, sphinx, etc). However you must always have a README! Lost for words? Add a title, usage, and/or link to your full documentation.

## Virtual Environment

|                    |                                                                  |
| ------------------ | ---------------------------------------------------------------- |
| `./package/.venv/` | The virtual environment. This does not have to be in the project |

It has not been said enough that for every project, you should have a reserved virtual environment for that project. This prevents the headache of having to make sure your Python's base environment plays well with all the other projects you may have.

There are various tools to create and manage virtual environments (e.g., [venv](https://docs.python.org/3/library/venv.html), [pipenv](https://pipenv.pypa.io/en/latest/), [poetry](https://python-poetry.org/)).

The virtual environment does not have to be in your project folder (recommended for organization and easy access). Another common place is `~/.local/share/virtualenvs/PROJECT_NAME`. Most virtual environment tools have options to change this.

## The init file

|                         |           |
| ----------------------- | --------- |
| `./package/__init__.py` | Init file |

Quick review, the init file (`__init__.py`) is always ran whenever you import the package. Depending on your experience with Python, you may or may not have the used the init file (`__init__.py`). It is perfectly fine to keep it empty. However if you were to take a look at any package, this file is quite heavily used in many ways:

1. **Indicate Package**
   An empty init file is widely used by many program to indicate the direction is a Python package.

2. **Forward Variables**
   Arguably the most important purpose of the init file, it is very common to see variables from the package modules forwarded to the init file.

   ```py
   # __init__.py
   from main import ClassA
   from helpers import helper_func
   ```

   That way you can designate the "main things" your user should be accessing. For instance,

   ```py
   from project import ClassA, helper_func
   ```

3. **Store Global Variables**
   Becauses the init file is always ran whenever you import the package, the variables inside the init file are also accessible by the package modules

   ```py
   # main.py
   from . import GLOBAL_VAR
   ```

   ```py
   # __init__.py
   GLOBAL_VAR = ...

   from main import ClassA
   ```

   Do be careful about circular dependency. The example above has `main.py` depending on the init file and the init file imports `main.py`. This example is not in conflict because of its sequential procedure and the init file is always first called: (1) `GLOBAL_VAR` is defined; (2) `main` is imported; (3) `main` imports `GLOBAL_VAR`; (4) `ClassA` is imported.

## Setup File

|              |                                |
| ------------ | ------------------------------ |
| `./setup.py` | The package specification file |

## Testing

|            |                       |
| ---------- | --------------------- |
| `./tests/` | The folder of test(s) |

Unfortunately because the test files are inside a directory different than your package, the test file not be able to directly import your package as a local package. Before I delve into the methods, it's best to establish the workflow we want to have.

It's would also be nice to run it at `./test/` in case we need to quickly modify the test directory.
Most intuitively, we like to run our test in the project folder.

```sh
# Run in project folder
python tests/main_test.py

# Run in test folder
python main_test.py
```

We also like to have the most intuitive package imports inside our test files:

```python
# main_test.py
import package
from package import main
```

There's aboslutely no reason you need to fuss around with relative imports (e.g., `from . import package`) because that should only be used in package files.

### Solutions to Test and Python Path Dependencies

Now, there are various ways to solve this issue and achieve this workflow floating around in the Python community:

- **Modify Python's Module Path (NOT RECOMMENDED)**
  There is also a few ways of doing this:

  1. Modify Python's `sys.path` on top of your test files

     ```python
     # main_test.py
     import sys
     from pathlib import Path

     # Highly recommended keeping this global variable almost everywhere
     PROJECT_PATH = Path(__file__).resolve().parents[1]
     # Inserting to the beginning of `sys.path` list to give overwriting priority
     sys.path.insert(0, str(PROJECT_PATH))

     # Everything else
     import package

     def main_test():
           ...
     ```

     Another implementation using `os` instead of `pathlib` is found in [samplemod from Kenneth Reitz et al.](https://github.com/navdeep-G/samplemod/tree/master/tests)

  2. Set `PYTHONPATH` environment variable

     ```sh
     export PYTHONPATH="/path/to/Project/"
     ```

     Alternatively,

     ```sh
     PYTHONPATH="/path/to/Project/" python test/test.py
     ```

  While this method is widely suggested (e.g., [Hitchiker's Guide](https://docs.python-guide.org/writing/structure/#test-suite), [StackOverflow](https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure)), I do not recommend this because (1) is quite tedious or complex to incorporate onto all your test files and (2) again very tedious to incorporate everywhere. This method seems to be a hotfix and inspire a bad habit of being ignorant of how Python should find packages.

- **Test Directory inside Package (NOT RECOMMENDED)**
  Instead of having the test directory on the root level, some prefer to place it inside the package

  ```
  /Project/
     /project/
        __init__.py
        ...
        /test/
           main_test.py
           ...
      ...
  ```

  This is a matter of your own preference. To me, the test do not belong to the package as it will also be included in the bundled Python package for your users to install. When projects become very complex, it's best to have all primary components of the project to be clearly displayed on the root level.

- **Installing the Local Package (RECOMMENDED)**
  Most natural way of having your package available to you is to install it. Make sure your have a proper `setup.py` and you're installing it into your virtual environment.

  ```sh
  pip install -e .
  ```

  The `-e` flag or `--editable` is meant for installing local packages. Any changes to your local package will reflect onto your python environment. If you really want a snapshot of your package instead, remove this flag.

- **Using Test Tools (RECOMMENDED)**
  The recommended solution along with the need to adopt a test framework is to use the available testing packages out there. There are various testing packages out there like the official Python's [unittest](https://docs.python.org/3/library/unittest.html) and [pytest](https://docs.pytest.org/en/latest/). These testing packages automatically resolve local package dependencies

  ```sh
  # unittest
  python -m unittest test.main_test

  # pytest
  pytest test/main_test
  ```
