---
title: Python 3.6
---

Here lists the new features since Python 3.5 adopted or to be adopted into my codes.

## f-Strings

|                              |                                                      |
| ---------------------------- | ---------------------------------------------------- |
| Literal String Interpolation | [PEP 498](https://www.python.org/dev/peps/pep-0498/) |

One of the most fundamental changes in string representation is the ease of us given by f-strings (f for format).

```python
from math import pi

# Suffixes are Precision
precision = 3
print(f"Three values of pi {pi:.{precision}}") // 3.14
print(f"Three significant figures of pi {pi:.{precision}g}") // 3.14
print(f"Three decimals of pi {pi:.{precision}f}") // 3.141



# String Size (default align right)
width = 5
print(f"{pi:{width}.{precision}") //  3.14

# Prefixes are formats
# Exponential
print (f"{pi:e}") # 3.141593e+00
```

## Variable Type Syntax

|                                 |                                                      |
| ------------------------------- | ---------------------------------------------------- |
| Syntax for Variable Annotations | [PEP 526](https://www.python.org/dev/peps/pep-0526/) |
| Type Hints                      | [PEP 484](https://www.python.org/dev/peps/pep-0484/) |

```py
from typing import Dict

d: Dict[str, int] = {}
```

## Underscore Numerical Separator

|                                 |                                                      |
| ------------------------------- | ---------------------------------------------------- |
| Underscores in Numeric Literals | [PEP 515](https://www.python.org/dev/peps/pep-0515/) |

Allow arbritrary underscore (`_`) placement between numbers as separators.

```py
addr = 0xCAFE_F00D  # 3405705229
0xCAFE_F00D == 0xCAFEF00D # True
```

## Async Generators

|                                        |                                                      |
| -------------------------------------- | ---------------------------------------------------- |
| Asynchronous Generators                | [PEP 525](https://www.python.org/dev/peps/pep-0525/) |
| Coroutines with async and await syntax | [PEP 492](https://www.python.org/dev/peps/pep-0492/) |

```py
async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)
```

## Async Comprehension

|                            |                                                      |
| -------------------------- | ---------------------------------------------------- |
| Asynchronous Comprehension | [PEP 530](https://www.python.org/dev/peps/pep-0530/) |

Adds `async for` in list, set, dict comprehension and genrator expression:

```py
result = [i async for i in async_iterator() if i % 2]
```

Adds `await` for all kinds of comprehension:

```py
result = [await fun() for fun in funcs if await condition()]
```

## Simpler Subclass Creation and Customization

```py
class Philosopher:
    subclasses = []
    def __init_subclass__(cls, default_name, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.default_name = default_name
        Philosopher.subclasses.append(cls)

class AustralianPhilosopher(Philosopher, default_name="Bruce"):
    pass
```

## File System Path Protocol

|                                    |                                                      |
| ---------------------------------- | ---------------------------------------------------- |
| Adding a file system path protocol | [PEP 530](https://www.python.org/dev/peps/pep-0530/) |

Historically, a path-like object must either be a `str` or `bytes`. However with the use of other path-like objectss like those in `pathlib`, a protocol is implement to more easily incorporate other path-like objects.

- `os.PathLike` is an abstract base class that inherits functions in `os` and `os.path` modules.
- `open()` make take in all `os.PathLike` objects (e.g., `pathlib`)

## Preserving Order of Class Attribute and Kwargs

[PEP 520](https://www.python.org/dev/peps/pep-0520/)
[PEP 468](https://www.python.org/dev/peps/pep-0468/)

`__dict__` in classes and `\*\*kwargs`` in function now preserve insertion order.

## Dictionary Implementation

- `dict` uses 20% to 25% less memory
- `dict` is ordered by implementation detail, **not permanent**!
