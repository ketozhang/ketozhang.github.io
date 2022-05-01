---
title: C++ with Pybind11
---

## Setup
```sh
$ pip install pybind11
```

```cpp
#include <pybind11/pybind11.h>
namespace py=pybind11
```

```py
from setuptools import find_packages, setup
from pybind11.setup_helpers import build_ext, intree_extensions

ext_modules = intree_extensions(["path/to/mypkg/mypkg.cpp"])

setup(
    name="mypkg",
    version="0.0.0",
    cmdclass={"build_ext": build_ext},  # Uses latest C++ standard
    ext_modules=ext_modules,
)
```

## Numpy
For most usage of numpy, you'll need to include the `pybind11/numpy.h` header.

### Numpy to Pointer Arrays
Since we're dealing with pointers, this can be done without copying

```cpp
// Adds two 1D double arrays.
void AddPtrArr(const double *x, const double *y, size_t size, double *z) {
  for (size_t i = 0; i < size; i++) {
    z[i] = x[i] + y[i];
  }
}

py::array_t<double> AddNumpy(const py::array_t<double> &x,
                              const py::array_t<double> &y) {
  // Assumes x and y are of same size and dimension of 1
  size_t s = x.size();
  auto result = py::array_t<double>(s);

  // We can pass in the input arrays' pointers to the first element
  // and pass the output array as a non-const pointer.
  AddPtrArr(x.data(), y.data(), x.size(), result.mutable_data());
  return result;
}
```

### Numpy to Vectors
Unfortunately C++ vector never was able to ingest pre-allocated arrays without copying.

```cpp
// Adds two 1D double vectors.
vector<double> AddVector(const vector<double>& x, const vector<double>& y) {
  vector<double> z;
  for (size_t i = 0; i < x.size(); i++) {
    // Assumes x.size() == y.size()
    z.push_back(x[i] + y[i]);
  }
  return z;
}

py::array_t<double> AddNumpy(const py::array_t<double> &x,
                              const py::array_t<double> &y) {
  // Assumes x and y are of same size and dimension of 1
  size_t s = x.size();

  // Copy numpy array elements to new vectors
  vector<double> x_vec;
  x_vec.insert(x_vec.end(), &x[0], &x[x.size()])
  vector<double> y_vec;
  y_vec.insert(y_vec.end(), &y[0], &y[y.size()])

  vector<double> result = AddVector(x.data(), y.data());

  // Cast the vector to numpy
  py::array_t<double> result_numpy = py::cast(result)
  return result_numpy;
}
```