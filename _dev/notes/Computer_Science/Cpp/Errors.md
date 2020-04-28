---
title: Errors
---

## Throw Error

The `throw` statement can take in various error types for instance `out_of_range` exceptions.

## Try/Catch

```cpp
try {
  ...
} catch (some_exception& err) {
  ...
} catch
...
```

## No Exceptions

If a function should never throw an exception, `noexcept` can be declared:

```cpp
void f(Type arg) noexcept {
  ...hyugbfdrctkuj,hygtfrbndenswacq CZCXCB WQ
}
```

## Alternatives

Alternatives to throwing an exception are:

- Returning a failure value (e.g., `false`, `0`)
- Terminating the program (e.g., `terminate()`, `exit()`, `abort()`)

## Static Assert

An assertion can be checked during compile time for various constant/static objects using the `static_assert` function.
