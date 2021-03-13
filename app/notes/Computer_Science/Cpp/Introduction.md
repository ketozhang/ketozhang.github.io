---
title: Introduction
---

## Compile and Run Structure

- `.cpp`: The source file
- `.o`: The compiled file
- `.[EXECUTABLE]`: Executable file

## Hello World!

As usual with some imports.

- Notice that the return type of the main function is `int` instead of `void` (never use `void` for this).
- Notice the unique print to console syntax

```cpp
#include <iostream> // import I/O library
using namespace std; // No need to specify `std`

int main() {
	// prints "Hello World!" to console
	cout << "Hello, World!\n"; // More verbose, `std::cout`
}
```

## Function

```cpp
TYPE NAME([TYPE [ARG1], ...]) {
	// body
}
```

For example,

```cpp
double square(double x) {
	return x * x;
}


```

Features

- Function overloading, allow synonyms with different type

## Variables

Features

- Type declaration
- Various ways of initialization

  ```cpp
  type var = value;
  type var {value};
  type var = {value};
  class<type> var = {values, ...};
  ```

- Loss of information through conversion using `=`. Use the list form `{}` instead to error out when conversion occurs.
- Implicit type `auto` (e.g., `auto b = true`) will automatically use the initialization to determine the type.
- Constants supported `const` (run-time constant) and `constexpr` (compile-time constant). The latter is used for performance and memory corruption reasons which applies very strict requirements (e.g., immutability) on functions with `constexpr`.

## Basic Types

There are many basic types for example:

```cpp
bool
char
int
double
unsigned
```

## Arithmetic

All syntax is similar to Python.

Features

- Meaningful conversion between types (e.g., addition between int and double is double unless referenced by an int variable) preserves the highest precision.
- Increment (`++x`) and decrement (`--x`).

## Scope

There are four scopes:

1. Local scope
2. Class scope
3. Namespace scope
   A namespace is the point where the declaration is called to the end of the namespace (often end of the running file)
4. Global scope
   Everything else

## Pointers, References, and Arrays

An array is a collection of data available to all types:

```cpp
char s[3];
int numbers[2];
```

The pointer-object relation can be established by,

```cpp
char v[] = {"H", "E", "L", "L", "O"}

char* ptr_h = &v[0] // ptr_h points to address that is the 0th index of v (i.e., address of "H")
char* ptr_h2 = ptr_h1 // ptr_h2 points to the same address as ptr_h
char h = *ptr_h // h is the content of ptr_h (i.e., "H")

char& ref_h = v[0] // ref_h references to the address that is the 0th index of v (i.e., address of "H")
char& ref_e = v[1]
ref_e = ref_h // v is now has "HHLLO" because reference assignments auomatically dereference
              // without needing *
void func(char& s) {} // Pass by reference, the argument s will be the object instead of a copy.
```

Therefore there is a deep copy of an array is exprsesed as,

```cpp
int[] deepcopy(int[] arr) {
    int[sizeof(arr)] copy_arr;

    for (auto i=0; i!=sizeof(arr); ++i) {
        copy_arr[i] = arr[i];
    }

    return copy_arr;
}

int[] shallowcopy(int[] arr) {
    int[sizeof(arr)] copy_arr;

    for (auto i=0; i!=sizeof(arr); ++i) {
        copy_arr[i] = &arr[i];
    }
    return arr
}
```

**Features**

- Declaration Operators

  A declaration operator is a suffix unary operator taht determines whether the variable is an object, pointer, or reference:

  ```cpp
  Type arr[n] // arr is an array of n Type objects
  Type* ptr  // ptr is a pointer to a Type object
  Type& ref // ref is a reference to a Type object
  TypeA func(TypeB) // func is a function taking in TypeB object and returning TypeA object
  ```

- Null Pointer

  All pointers need to point to something so all dereference is valid. A pointer will point to a null pointer whenever initialized as so,

  ```cpp
  Type* ptr = nullptr;
  ```

## Control Statements

Standard if, for, and while are provided.

**Features**

- Switch cases, each `case` is ran until `break` otherwise `default` if exists or `pass`.
- Define variables inside statements:

  ```cpp
  bool var = true;
  if (auto cond=var; var) {
      ...
  }

  // Equivalently
  if (auto cond=var) {
      ...
  }
  ```
