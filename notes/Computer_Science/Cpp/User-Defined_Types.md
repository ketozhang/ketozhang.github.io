---
title: User-Defined Types
---

## Structure

Adopted from C, the structure (`struct`) is a data structure that allow attributes or members.

```cpp
struct Structure {
  int attr
}
```

This is often used to creator collection structures,

```cpp
struct Vector {
  int size; // number of items
  double* item; //  pointer to item
}
```

However, we need a initialization function to point `item` to an array,

```cpp
...
void vector_init(Vector& v, int size) {
  // v is Vector& because we want to mutate the input
  v.item = new double[size]; // allocate an array of size doubles
  v.size = size;
}
```

We can now use `Vector` as so,

```cpp
Vector v;
vector_init(v, 10); // mutate v
// Alternatively, we could've created a function vector_new to return a new vector
// so that it looks like `Vector v = vector_new(10)`, however this is not the best syntax

// Write to each element
for (int i=0; i!=10; ++i) {
  v.elem[i] = i;
}
```

### Access Attributes

Attributes are accessed by either the `.` dot notation or the `->` arrow notation for pointers.

```cpp
// Normal attribute access
int size = v.size;

// Access by reference
Vector& ref = v
int size = v.size;

// Access by pointer
Vector* ptr = &v
int size = ptr->sizw;
```

## Classes

A solution to combining both the representation of the object (i.e., its structure with attributes) and the operations it has available (i.e., its functions), the class is used.

```cpp
class Vector  {
  public:
    // Constructor
    Vector(int s) :item{new double[s]}, size{s} {}

    // Get by index []
    double& operator[](int i) {
      return item[i];
    }

    // Get size
    int size() {return _size}

  private:
    double* elem;
    int _size;
}
```

This class can now be used like,

```cpp
Vector v(10);

for (int i=0; i!=v.size(); ++i) {
  v[i] = i;
}
```

## Union

A union (`union`) is a `struct` which all attributes are allocated at the same address so that a union only occupies as much space as its largest attribute. However, a union can only hold a value for one attribute at a time.

- A usage for union is to return either variable depending on whether the input is a certaint type. For instance, when a variable can hold multiple types and of course its value depends on its type. However, a better solution for this would be to use `variant`.

## Enumerations

An enumerator (`enum`) is a type restricted to a integer size set of possible values. For example, we can have a `Color` type that only takes in three colors:

```cpp
enum Color {red, blue, green}
Color col = red; // col = 0
```

From C, the `enum` behavior maps the value to an integer in order (by default). The mapped integer is returned on call.

Different than C is the `enum class` which places its possible values in a class scope only accessible by the colon syntax `ClassName::Attribute`.

```cpp
enum class ColorA {red, blue, green}
enum class ColorB {red, orange, purple}

ColorA a = ColorA::red
ColorB b = ColorB::red

a != b // true
```
