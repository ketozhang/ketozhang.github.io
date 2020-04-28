---
title: Imports
---

## Header File

The header file is the file to be imported. In general, the header file defines all able imported. For instance, the class `Vector` has its functions defined in `Vector.cpp` but its declaration in the header file `Vector.h`.

## Modules

Due to various problems and limitations of header files, C++20 adopted modules where the interface declaration and definiton are in the same `.cpp` file.

## Namespaces

A namespace (`namespace`) can be defined to isolate code so that their names don't conflict with the global namespace.

Here, `ns` is a namespace so that `int` are not in conflict by requiring the double colon syntax `ns::int`.

```cpp
namespace ns {
  class int {
    ...
  };
}

int main() {
  ns::int var;
}
```

### Global Namespace

A namespace is imported into the global namespace by the `using` statement,

```cpp
using std // Use all of std
using std::cout // Use only std::cout
```
